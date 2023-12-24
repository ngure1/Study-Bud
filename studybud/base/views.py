from django.shortcuts import render
from . import models
from . import forms

rooms=models.Rooms.objects.all()

def home(request):
  context={'rooms':rooms}
  return render(request, 'base/home.html', context)

def room(request,pk):
  room=models.Rooms.objects.get(id=pk)
  context={'room':room}
  return render(request,'base/room.html',context)
  
def createRoom(request):
  form=forms.RoomsForm()
  context={'form':form}
  return render(request,'base/createroom.html',context)