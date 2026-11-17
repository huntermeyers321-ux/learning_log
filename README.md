# Learning Log

Django Project I for MIS 4357. An online journal: register, log in, create topics,
and add dated entries under each topic. Each user only sees their own topics.

Built with Django 4.0 and django-bootstrap4 on Python 3.11.

## Run it on a new computer (Windows)

Open the folder in VS Code, open a terminal (Terminal > New Terminal), then:

```
py -3.11 -m venv django_venv
django_venv\Scripts\activate
pip install -r requirements.txt
py manage.py runserver
```

Then open http://127.0.0.1:8000 in a browser. Press CTRL+C in the terminal to stop the server.

On a Mac the same four steps are:

```
python3.11 -m venv django_venv
source django_venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Python 3.11 is required. Django 4.0 does not run on Python 3.13.

## Where things are

| File | What it does |
|---|---|
| `learning_log/settings.py` | Project settings: installed apps, allowed hosts, login URL |
| `learning_log/urls.py` | Parent URL file. Includes the URLs of both apps |
| `MainApp/models.py` | The two database tables: Topic and Entry |
| `MainApp/urls.py` | URL for each page of the journal |
| `MainApp/views.py` | One function per page. Gets or saves data, then renders a template |
| `MainApp/forms.py` | TopicForm and EntryForm |
| `MainApp/templates/MainApp/` | HTML pages for the journal |
| `users/urls.py`, `users/views.py` | Log in, log out, register |
| `users/templates/registration/` | Log in, logged out, and register pages |
| `testcode.py` | Practice queries against the database. Not part of the site |
| `requirements.txt`, `start.sh` | Used by Render to install and start the live site |
