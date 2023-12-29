# Table of contents
- [What is CRUD](#what-is-crud)
- [Create](#create)
- [Read](#read)
- [Update](#update)
- [Delete](#delete)

## What is CRUD?
CRUD is an acronym for Create Read Update and Delete.<br>
Crud functionalities allow users to iteract with the database without necessarily having to use the django admin site

## Create
Creation of objects(because our models are classes when we instanciate them we are creating objects) in django can be done in two ways based off the type of form we used:
1. A user created form where the user codes the html form for themselves.
```html
<form method="post" action="">
    {% csrf_token %}
    <!-- Host -->
    <label for="host">Host:</label>
    <input type="text" name="host" required>
    <!-- Topic -->
    <label for="topic">Topic:</label>
    <input type="text" name="topic" required>
    <!-- Name -->
    <label for="name">Name:</label>
    <input type="text" name="name" required>
    <!-- Description -->
    <label for="description">Description:</label>
    <textarea name="description" rows="4" cols="50"></textarea>
    <!-- Submit Button -->
    <input type="submit" value="Create Room">
</form>
```
1. A django form (which we discussed earlier)<br>
``models.py```
```python
from django.db import models
#room model
class Room(models.Model):
  host=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  topic=models.ForeignKey('Topic',on_delete=models.SET_NULL,null=True)
  name=models.CharField(max_length=200)
  description=models.TextField(null=True,blank=True)
  participants=models.ManyToManyField(User,related_name='participants')
  created=models.DateTimeField(auto_now_add=True)
  updated=models.DateTimeField(auto_now=True)
```
``forms.py``
```py
from django.forms import ModelForm
from models import Room
#creating a roomform with all rields included
class RoomForm(ModelForm):
  class Meta:
    model = Room
    fields = '__all__' 
```
The difference between the two forms is that when we use the model forms we have the option to do operations such as ``form.is_valid`` and ``form.save()`` however when we use our own forms we dont have such methods although I will later show you how we can get the best of both words by allowing ourselves to have those methods and the form stiil be user created<br>
Most of the logic behind it will be handled in the ``views.py``.<br>
- If you use manually created forms:
```py
from forms.py import RoomForm
from models import Room
from django.shortcuts import render,redirect

def createRoom(request):
  if request.method=='POST':
    room=Room.objects.create(
      host = request.POST.get('host')
      topic = request.POST.get('topic')
      name = request.POST.get('name')
      description = request.POST.get('description')
    )
    room.save()
    return redirect('home.html')
  return render (request,'create_room_form.html')
```
- If you use model forms:
```py
from forms.py import RoomForm
from django.shortcuts import render,redirect

def createRoom(request):
  #instanciate the form with empty fields
  form=RoomForm()
  #check if the user clicked submit
  if request.method=='POST':
    #initialise the formwith the data the user entered in the input field
    form= RoomForm(request.POST)
    #check if form is valid
    if form.is_valid:
      form.save()
      #redirect the user back to the home page
      return redirect('home')
  #passing the form in the context dictionary so we can render it in the template
  context={'form':form}
  return render(request, 'yourtemplate.html',context)
```
### How to get the both of both worlds
How this will work is that we use a model form but when rendering the form we create a user form but without input fields we will render the input fields from the model form
```html
<form method="POST" action="">
  {{form.label}}
  {{form.host}}
</form>
```

## Read
To read you just have to render the room objects in the templates.<br>
- Querry all the room objects in the views
- Render them in the template 

```python
def readRooms(request):
  rooms=Room.objects.all()
  context={'rooms':rooms}
  return render(request,'RoomRenderingTemplate',context)
```
In the template
```html
{% for room in rooms %}
<small>@{{room.host}}</small>
{{room.topic}}
{{room.name}}
{{room.description}}
<hr>
{% endfor %}
```

## Update
