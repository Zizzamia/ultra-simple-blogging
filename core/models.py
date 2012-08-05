# -*- coding: utf-8 -*-
"""
models.py
~~~~~~

"""
from google.appengine.ext import db

class Post(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty()
    date = db.DateTimeProperty(auto_now_add=True)