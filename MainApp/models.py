from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# A model is a class that represents one TABLE in the database.
# Django adds a hidden "id" column (the primary key) to every model for us.


class Topic(models.Model):
    """A topic the user is learning about, for example Chess."""
    text = models.CharField(max_length=200)
    # auto_now_add=True fills in the current date and time automatically
    # when a new topic is created.
    date_added = models.DateTimeField(auto_now_add=True)
    # Every topic belongs to one user. This is how each person only sees
    # their own journal (Topic 14, video 5).
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Show the topic's text instead of 'Topic object (1)'."""
        return self.text


class Entry(models.Model):
    """Something specific the user learned about a topic."""
    # Foreign key = the link between the two tables. One topic can have
    # many entries (a one-to-many relationship). CASCADE means that if a
    # topic is deleted, its entries are deleted too.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # TextField has no length limit, so an entry can be several paragraphs.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Without this, the admin site would call them "Entrys".
        verbose_name_plural = 'entries'

    def __str__(self):
        """Show only the first 50 characters of the entry."""
        return f"{self.text[:50]}..."
