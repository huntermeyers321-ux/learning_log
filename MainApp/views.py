from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
# A view is a function that receives a request, gets or saves data in the
# database, and sends back a page built from a template.
#
# @login_required is a decorator. It runs before the view and sends anyone
# who is not logged in to the log in page (LOGIN_URL in settings.py).


def index(request):
    """The home page for Learning Log. Open to everyone."""
    return render(request, 'MainApp/index.html')


@login_required
def topics(request):
    """Show all topics that belong to the logged-in user."""
    # filter(owner=request.user) = only this user's topics.
    # order_by('date_added') = oldest first.
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # The context dictionary passes data to the template. The KEY is the
    # variable name used in the template, the VALUE is the data.
    context = {'topics': topics}
    return render(request, 'MainApp/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all of its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user. Without this check,
    # someone could type topics/2/ in the address bar and read another
    # user's journal.
    if topic.owner != request.user:
        raise Http404

    # The minus sign sorts newest entries first.
    entries = Entry.objects.filter(topic=topic).order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'MainApp/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # GET request: no data submitted, so show a blank form.
        form = TopicForm()
    else:
        # POST request: the user filled in the form and pressed the button.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # commit=False builds the topic object WITHOUT saving it yet,
            # so we can attach the owner first.
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('MainApp:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    # Practice problem 14.1: only the owner may add entries to a topic.
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # The form only has the text. The entry also needs to know
            # which topic it belongs to before it can be saved.
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic', topic_id=topic_id)

    context = {'form': form, 'topic': topic}
    return render(request, 'MainApp/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    # topic is an attribute of the entry, so we can reach it from the entry.
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # instance=entry fills the form with the text that is already saved.
        form = EntryForm(instance=entry)
    else:
        # instance=entry plus the new data = update the SAME row.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'MainApp/edit_entry.html', context)
