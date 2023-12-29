from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Rooms(models.Model):
  host=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  topic=models.ForeignKey('Topic',on_delete=models.SET_NULL,null=True)
  name=models.CharField(max_length=200)
  description=models.TextField(null=True,blank=True)
  participants=models.ManyToManyField(User,related_name='participants',blank=True)
  created=models.DateTimeField(auto_now_add=True)
  updated=models.DateTimeField(auto_now=True)


  class Meta:
    ordering=['-updated','-created']
    verbose_name="Room"
    verbose_name_plural="Rooms"
    db_table="Room Table"

  
  def __str__(self):
    return self.name

class Messages(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
  body=models.TextField()
  updated=models.DateTimeField(auto_now_add=True)
  created=models.DateTimeField(auto_now=True)
  class Meta:
    verbose_name="Message"
    verbose_name_plural="Messages"
    ordering=['-updated','-created']

  def __str__(self):
    return "@"+str(self.user.username) +" "+ self.body[0:10]

class Topic(models.Model):
  name=models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name="Topic"
    verbose_name_plural="Topics"
