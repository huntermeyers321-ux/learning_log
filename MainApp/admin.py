from django.contrib import admin

# The dot means "look for models.py in the same folder as this file".
from .models import Topic, Entry

# Register your models here.
# Registering a model makes it show up on the admin site (/admin).
admin.site.register(Topic)
admin.site.register(Entry)
