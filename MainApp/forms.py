from django import forms

from .models import Topic, Entry

# A ModelForm builds a form straight from a model, so we do not have to
# describe the fields a second time.


class TopicForm(forms.ModelForm):
    class Meta:
        # NOTE: "model" must be lowercase.
        model = Topic
        # Only ask the user for the text. date_added is automatic and
        # owner is set in the view.
        fields = ['text']
        # An empty label so the word "Text" does not show next to the box.
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # A widget is the HTML form element. Textarea with 80 columns gives
        # the user a bigger box to write an entry in.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
