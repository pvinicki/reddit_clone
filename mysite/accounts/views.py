from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            #log the user in
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            #log the user in

            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form':form})

