# Table of contents
- [Introduction](#introduction)
- [Queries](#queries)
  - [Querying related records](#querying-related-records)
  - [Querying against foreign keys](#querying-against-foreign-keys)
  - [Querying with related relations](#querying-with-related-relations)

## Introduction
Querying the database is the process of retrieving or manipulating the data in the database.<br>
This can be useful for displaying data in the templates.
The structure that the querrying the database takes is 
```
queryset = Model.objects.method()
```
The queryset is a variable that stores the data retrieved form the database.
The Model represents the model whose data you want to retrieve.
onjects refers to instances of the model
method() represents the specific method we want to use wich cn be either:
- ``all()`` - retrieves all objects of the particular model.**Note: Can be indexed just like a list to return records in a speific index or range**
- ``filter()`` - takes conditionals as arguments and returns the objects/records that meet that condition
- ``exclude()`` - works like filter but returns the objects/records that do not meet a condition
- ``get()`` - mostly used when we have dynamic urls to get the record/object whose id matches the pk(primary key) and also in [searching](./searchingandfiltering.md) 

**Example**
Assume the following model
```py
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
  host = models.OneToOneField(User,on_delete=models.CASCADE)
  room_name = models.CharField(max_length = 200)
  topic=models.ForeignKey('Topic',on_delete=models.SET_NULL,null=True)
  description=models.TextField(null=True,blank=True)
  participants=models.ManyToManyField(User,related_name='participants',blank=True)#we will work with this later
  created=models.DateTimeField(auto_now_add=True)
  updated=models.DateTimeField(auto_now=True) 

```
Now we will use some basic querries in views.py
```py
from .models import *
def basicQueries(request):
  #Getting all the rooms 
  rooms = Room.objects.all()
  #Getting all rooms with the 

```