from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

from . import forms
# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserSignUpForm
    # Setting form_class attribute equal to UserSignUpForm from forms without instantiating
    success_url = reverse_lazy('login')
    # On a successful login reverse back to the login page
    template_name = 'users/register.html'


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process the completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # Login the new user and redirect to homepage
            login(request, new_user)
            return HttpResponseRedirect(reverse_lazy('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
