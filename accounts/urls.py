from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('register', views.sign_up, name='Register'),
    path('login', views.sign_in, name='Login'),
    path('logout', views.log_out, name='Logout')
]
