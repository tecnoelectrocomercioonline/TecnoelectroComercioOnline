from django import forms
from .models import *

class HomeForm(models.Model):
    name = forms.CharField(max_length=25, null=False)
    email = forms.CharField(max_length=50, null=False)
    subject = forms.TextField(max_length=30)
    message = forms.TextField(max_length=100)
