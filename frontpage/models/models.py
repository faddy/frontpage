'''
Created on Sep 18, 2013

@author: fahad
'''
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    
    
class Source(models.Model):

    source_choices = ('other', 'rss', 'url')
   
    source_type = models.CharField(max_length=10, choices=source_choices, default='url')
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    source = models.CharField(max_length=100)    # actual url or rss url
    
    category = models.ForeignKey(Category)
    
    
class Post(models.Model):
    
    post_choices = ('image', 'video', 'url')

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    post_type = models.CharField(max_length=10, choices=post_choices, default='url')
    action = models.CharField(max_length=10)
