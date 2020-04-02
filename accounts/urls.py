from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('register', views.register, name='Register')
]
