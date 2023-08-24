from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                message = 'Login failed!'
    context = {
        'form': form, 
        'message': message
    }
    return render(request, 'user_operations/login.html', context)

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, "user_operations/sign_up.html", context)

def logout(request):
    print('logoutbutton pressed')
    if request.user.is_authenticated:
        print('user authorize true')
        logout(request)
    return render(request, 'user_operations/sign_up.html')
