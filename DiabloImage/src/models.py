#coding:utf-8
from google.appengine.ext import db
class Images(db.Model):
    name = db.StringProperty()
    mime = db.StringProperty()
    size = db.IntegerProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    comment = db.StringProperty()
    bf = db.BlobProperty() #binary file
    
    def save(self):
        self.put()
        
    def de(self):
        self.delete()