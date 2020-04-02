from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)
