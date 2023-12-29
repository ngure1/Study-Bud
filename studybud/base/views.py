from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect,HttpResponse

from . import models
from . import forms

def signUp(request):
  form = forms.signUp()
  if request.method=='POST':
    username=request.POST.get('username')
    try:
      models.User.objects.get(username=username)
      messages.warning(request,"Username is already taken")
    except ObjectDoesNotExist:
      form=forms.signUp(request.POST)
      if form.is_valid:
        form.save()
        return redirect('login')
  context={'form':form}
  return render(request,'base/signUp.html',context)


def loginView(request):

  if request.user.is_authenticated:
    return redirect('home')
  if request.method =='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    try:
      user=User.objects.get(username=username)
    except:
      messages.error(request,"User does not exist")
    user=authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.error(request,"Username or password does not exist")
  context={}
  return render(request , 'base/login.html', context)


def logoutView(request):
  logout(request)
  return redirect ('home')


def home(request):
  q=request.GET.get('q') if request.GET.get('q') != None else ''
  rooms=models.Rooms.objects.filter(
    Q(topic__name__icontains=q) |
    Q(name__icontains=q) |
    Q(host__username__icontains=q)
    )
  room_messages=models.Messages.objects.all()
  topics=models.Topic.objects.all()
  room_count=rooms.count()
  context={
    'rooms':rooms,
    'topics':topics,
    'room_count':room_count ,
    'room_messages':room_messages
           }
  return render(request, 'base/home.html', context)

@login_required(login_url='login')
def room(request,pk):
  room=models.Rooms.objects.get(id=pk)
  room_message=room.messages_set.all()
  participants=room.participants.all()
  if request.method=='POST':
    room_message=models.Messages.objects.create(
      user=request.user,
      room=room,
      body=request.POST.get('body')
    )
    room.participants.add(request.user)
    return redirect('room',pk=room.id)
  context={
    'room':room,
    'room_message':room_message,
    'participants':participants
    }
  return render(request,'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
  form=forms.RoomsForm()
  if request.method == 'POST':
    form=forms.RoomsForm(request.POST)
    if form.is_valid:
      form.save()
      return redirect('home')
  context={'form':form}
  return render(request,'base/createroom.html',context)

@login_required(login_url='login')
def updateRoom(request,pk):
  room =models.Rooms.objects.get(id=pk)
  form=forms.RoomsForm(instance=room)

  if request.user != room.host:
    return HttpResponse('You are not allowed here')
  
  if request.method=='POST':
    form=forms.RoomsForm(request.POST,instance=room)
    if form.is_valid:
      form.save()
      return redirect('home')
  context={'form':form}
  return render(request, 'base/createroom.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
  room=models.Rooms.objects.get(id=pk)

  if request.user != room.host:
    return HttpResponse('You are not allowed here')
  
  if request.method=="POST":
    room.delete()
    return redirect ('home')
  return render(request ,'base/delete.html',{'obj':room})

def deleteMessage(request,pk):
  message=models.Messages.objects.get(id=pk)
  if request.user != message.user:
    return HttpResponse('You cannot delete this message')
  if request.method =='POST':
    room=message.room
    message.delete()
    return redirect('room',pk=room.id)
  return render(request,'base/delete.html',{'obj':message.body})


def userProfile(request,pk):
  topics=models.Topic.objects.all()
  user=User.objects.get(id=pk)
  room_messages=user.messages_set.all()
  rooms=user.rooms_set.all()
  context={'user':user,
           'topics':topics,
           'room_messages':room_messages,
           'rooms':rooms
           }
  return render(request,'base/user_profile.html',context)