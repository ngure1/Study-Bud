from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . import models

class RoomsForm(ModelForm):
  class Meta:
    model=models.Rooms
    fields='__all__'
    exclude=['host','participants']


class signUp(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email','password1','password2']