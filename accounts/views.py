from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'accounts/index.html')


def register(request):

    form = UserCreationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)
