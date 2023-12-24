from django.urls import path
from . import views

urlpatterns = [
  path('',views.home, name='home'),
  path('room/<str:pk>' , views.room, name='room'),
  path('createroom',views.createRoom, name='createroom'),
  path('updateroom/<str:pk>/',views.updateRoom,name='updateroom'),
  path('deleteroom/<str:pk>/',views.deleteRoom,name='deleteroom')
]