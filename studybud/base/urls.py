from django.urls import path
from . import views

urlpatterns = [
  path('signup/',views.signUp,name='signup'),
  path('login/',views.loginView,name='login'),
  path('logout/',views.logoutView,name='logout'),
  path('profile/<str:pk>/',views.userProfile,name='user-profile'),
  path('',views.home, name='home'),
  path('room/<str:pk>' , views.room, name='room'),
  path('createroom',views.createRoom, name='createroom'),
  path('updateroom/<str:pk>/',views.updateRoom,name='updateroom'),
  path('deleteroom/<str:pk>/',views.deleteRoom,name='deleteroom'),
  path('deletemessage/<str:pk>/',views.deleteMessage,name='deletemessage')
]