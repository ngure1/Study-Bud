# Table of contents
- [Django Forms](#django-forms)
- [Django Model Forms](#django-model-forms)

## Django Forms
Django form provides a form class which is used to create HTML forms.
It is similar to model forms but unlike model forms which makes forms based off the fields in the model the user has the liberty to choose the fields they would like in the form.
Each field maps to the ``HTML`` input element each of which is a class itself, it manages form data and performs validation while submiting the form.
**Note :** Inorder to work with a form you create a ``forms.py`` file in your app.

**Example**
In the created ``forms.py`` file
```python
  from django import forms
# Each form class inherits from forms.Form
  class StudentForm(forms.Form):
    first_name = forms.CharField(label="Enter Your First Name" , max_length=50)
    Last_name = forms.CharField(label="Enter Your Last Name" , max_length=50)
```
**Its html equivalent**
```html
    <label for="id_first_name">Enter Your First Name:</label>
    <input type="text" name="first_name" id="id_first_name" maxlength="50" required>

    <label for="id_last_name">Enter Your Last Name:</label>
    <input type="text" name="last_name" id="id_last_name" maxlength="50" required>
```

**MORE FORMS FIELDS**
|Field Name|Representation|
|---|---|
|BoleanField|checkbox (false=unchecked)|
|EmailField|email input|
|ChoiceField|select|
|DateField|date input|
|DateTimeField|date time input|
|DecimalField|number input|

## Django Model Forms
It is a class that us used to create a html form using the model.
**Example**<br>
In your app's ``models.py``
```py
  from django.db import models
  class Student(models.Model):
    First_name=models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    Date_of_birth=models.DateField()
```
In your app's ``forms.py``
```py
  from django.forms import ModelForm#all model forms inherit the ModelForm class
  from . import models#imports all the models from the app
  #You can alternatively import the specific model using:
  #from .models import Student
  class StudentForm(ModelForm):
    class Meta:
      model = models.Student
      fields='__all__'
      #you can alternatively select the fields you want to be included in the form by using a list of modelfields you want included
      #*fields=['First_name','Date_of_Birth']
```
