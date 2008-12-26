#coding:utf-8
import wsgiref.handlers
from google.appengine.ext import webapp

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Hi')

def main():
    application = webapp.WSGIApplication(
                                       [('/', MainPage)
                                       ], debug=True)
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()