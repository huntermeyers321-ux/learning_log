"""URL patterns for MainApp. Each URL points to one view function."""
from django.urls import path

# The dot means "import views.py from this same folder".
from . import views

# app_name lets templates say 'MainApp:topics' so Django knows which app
# the URL name belongs to.
app_name = 'MainApp'

urlpatterns = [
    # Home page. The empty string matches http://127.0.0.1:8000/
    path('', views.index, name='index'),

    # Page that shows all of the user's topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic. <int:topic_id> captures the number in
    # the URL (topics/1/) and passes it to the view as topic_id.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry to a topic.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
