from django.shortcuts import render,redirect
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
  if request.method == 'POST':
    form=forms.RoomsForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('home')
  context={'form':form}
  return render(request,'base/createroom.html',context)
def updateRoom(request,pk):
  room =models.Rooms.objects.get(id=pk)
  form=forms.RoomsForm(instance=room)
  if request.method=='POST':
    form=forms.RoomsForm(request.POST,instance=room)
    if form.is_valid:
      form.save()
      return redirect('home')
  context={'form':form}
  return render(request, 'base/createroom.html',context)

def deleteRoom(request,pk):

  room=models.Rooms.objects.get(id=pk)
  if request.method=="POST":
    room.delete()
    return redirect ('home')
  return render(request ,'base/delete.html',{'obj':room})