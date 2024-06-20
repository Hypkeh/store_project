from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User

from . import forms
# Create your views here.

class UserLogoutView(LogoutView):
    success_url = 'logout_view'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'  

def login_view(request):
    default_url = settings.LOGIN_REDIRECT_URL
    next_url = request.GET.get('next', default_url)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(next_url)
        else:
            return render(request, 'accounts/login.html', {'error': 'invalid username or password',
                                                           'form': AuthenticationForm()})
    else:
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})

def register(request):
    if request.method == 'POST':
        data = request.POST # request.GET = {'name': 'new_name'}
        form = forms.SignUpForm(data)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = forms.SignUpForm()
    return render(request, 'accounts/file_form.html', {'form': form})

def profile_view(request):
    username = request.user.username
    email = request.user.email
    context = {'username': username, 'email': email}
    return render(request, 'accounts/profile.html', context)
