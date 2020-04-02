from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('accounts/login')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def login(request):

    form = LoginForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)
