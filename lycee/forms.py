from django.forms.models import ModelForm
from django import forms
from .models import Student
from .models import Presence

class StudentForm(ModelForm):

  class Meta:
    # le modele auquel on se ReferenceError
    model = Student
    
    # les champs qu'on veut voir apparaitre dans le formulaire
    fields = (
      "first_name",
      "last_name",
      "birth_date",
      "email",
      "phone",
      "comments",
      "cursus"
    )

class PresenceForm(ModelForm):

  class Meta:
    # le modele auquel on se ReferenceError
    model = Presence
    
    # les champs qu'on veut voir apparaitre dans le formulaire
    fields = (
      "date",
      "isMissing",
      "reason",
      "student"
    )

#class AppelForm(ModelForm):

#  class Meta:
#    model = Presence

#    fields = ['date']
#    widgets = {
#      'date' : forms.DateInput(attrs={'type':'date'})
#    }

#  date = forms.DateInput()

class AppelForm(ModelForm):

  class Meta:
    model = Presence

    fields = ['date']
    widgets = {
      'date' : forms.DateInput(attrs={'type':'date'})
    }

  date = forms.DateInput()