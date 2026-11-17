from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process the completed form.
        form = UserCreationForm(data=request.POST)
        # is_valid() checks the username, that both passwords match, and
        # that the password is strong enough.
        if form.is_valid():
            # save() creates the new user and gives the user object back.
            new_user = form.save()
            # Log the user in and send them to the home page.
            login(request, new_user)
            return redirect('MainApp:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
