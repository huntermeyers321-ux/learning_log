"""URL patterns for the users app."""
from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # Include Django's default auth URLs. This gives us 'login' and 'logout'
    # without writing the views ourselves.
    path('', include('django.contrib.auth.urls')),

    # Registration page. This one uses our own view.
    path('register/', views.register, name='register'),
]
