from django.forms import ModelForm
from . import models

class RoomsForm(ModelForm):
  class Meta:
    model=models.Rooms
    fields='__all__'
