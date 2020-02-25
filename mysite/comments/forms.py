from django import forms
from django.contrib.admin import widgets  
  

class Post(forms.Form):
    title = forms.CharField(max_length = 200)
    text = forms.CharField(max_length = 500)


