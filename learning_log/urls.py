"""learning_log URL Configuration

This is the PARENT urls file for the whole project. Instead of listing every
page here, each app keeps its own urls.py and we "include" them.
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    # Django's built-in admin site: http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # Every URL that starts with users/ is handled by users/urls.py
    # (log in, log out, register).
    path('users/', include('users.urls')),

    # The empty string '' means the home page. Everything else is handled
    # by MainApp/urls.py (topics, entries).
    path('', include('MainApp.urls')),
]

# Lets the admin site keep its styling when the project runs on Render.
urlpatterns += staticfiles_urlpatterns()
