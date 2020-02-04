from django import forms

class Post(forms.Form):
    title = forms.CharField(max_length = 200)
    text = forms.CharField(max_length = 500)