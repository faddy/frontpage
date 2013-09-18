'''
Created on Sep 18, 2013

@author: fahad
'''
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    
    
class Source(models.Model):
    
    source_type = models.CharField(max_length=10)  # TODO: change this to enum: rss / url / something else?
    name = models.CharField(max_length=50)
    domain = models.CharField(max_length=100)
    source = models.CharField(max_length=100)    # actual url or rss url
    
    category = models.ForeignKey(Category)
    
    
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    type = models.CharField(max_length=10)    # TODO: change this to enum
    