# -*- coding: utf-8 -*-
"""
views.py
~~~~~~
All the views of the blog

"""
import logging
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect

from google.appengine.ext import db
from core.models import Post


def home(request):
    """ Home page with all the post """
    lastest_post = db.GqlQuery("SELECT * FROM Post ORDER BY date DESC")
    return direct_to_template(request, 'index.html', { "lastest_post": lastest_post})

def read_post(request, post_id):
    """ Read a post """
    post = db.get(post_id)
    return direct_to_template(request, 'read_post.html', {"post": post})

def create_post(request):
    """ Create a new post """
    local = {}
    
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            post = Post(title=title, content=content) 
            post.put()
            return HttpResponseRedirect('/')
        except:
            status = "msg msg-error"
            message = "Error: Create post"
            local = {
                "status": status,
                "message": message
            }
    
    return direct_to_template(request, 'create_post.html', local)

def edit_post(request, post_id):
    """ Edit a post """
    post = db.get(post_id)
    status = None
    message = None
    
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            content = request.POST.get('content')
            post.title = title
            post.content = content
            post.put()
            status = "msg msg-success"
            message = "Post edited successfully."
        except:
            status = "msg msg-error"
            message = "Error: Edit post"
            
    local = {
        "post": post, 
        "post_id": post_id,
        "status": status,
        "message": message
    }
    return direct_to_template(request, 'edit_post.html', local)

def delete_post(request, post_id):
    """ Delete a post """
    try:
        post_entity = db.get(post_id)
        post_entity.delete()
        return HttpResponseRedirect('/')
    except db.BadKeyError:
        data = {"success": False}
        return HttpResponseRedirect('/')

def exception_test(request):
    """ """
    logging.debug('Debug log')
    logging.warn('Warn log')
    logging.error('Error log')
    raise Exception()

