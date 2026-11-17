# testcode.py - practice file from Topic 12 (solution video).
# It is NOT part of the website. It lets us look at the database with Python.
# Run it with:  py testcode.py   (virtual environment must be active)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry
from django.contrib.auth.models import User

# Get every topic. Same idea as "SELECT * FROM topic" in SQL.
# What comes back is called a queryset.
topics = Topic.objects.all()

for t in topics:
    print(t.id, t.text, t.date_added)

# Get ONE topic by its id.
t = Topic.objects.get(id=1)

print(t)
print(t.date_added)

# Get only the entries that belong to that topic.
entries = Entry.objects.filter(topic=t)

for entry in entries:
    print(entry)

# List every user and their id (Topic 14, video 5).
for user in User.objects.all():
    print(user.username, user.id)
