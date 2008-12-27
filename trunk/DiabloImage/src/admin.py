#coding:utf-8
import wsgiref.handlers
import os
from functools import wraps
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users
import methods

class AdminControl(webapp.RequestHandler):
    def render(self,template_file,template_value):
        path=os.path.join(os.path.dirname(__file__),template_file)
        self.response.out.write(template.render(path, template_value))

def requires_admin(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return
        elif not users.is_current_user_admin():
            return self.error(403)
        else:
            return method(self, *args, **kwargs)
    return wrapper

class Admin_Upload(AdminControl):
    def get(self):
        self.render('views/upload.html', {})
    
    def post(self):
        bf=self.request.get("file")
        if not bf:
            return self.redirect('/admin/upload/')
#        name=self.request.body_file.vars['file'].filename
        mime = self.request.body_file.vars['file'].headers['content-type']
        description=self.request.get("description")
        image=methods.addImage( mime, description, bf)
        
        self.redirect('/show/'+image.imgname)

class Delete_Image(AdminControl):
    @requires_admin
    def get(self,key):
        methods.delImage(key)
        self.redirect('/')
        
def main():
    application = webapp.WSGIApplication(
                                       [(r'/admin/upload/', Admin_Upload),
                                        (r'/admin/del/(?P<key>[a-z,A-Z,0-9]+)', Delete_Image),
                                       ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()