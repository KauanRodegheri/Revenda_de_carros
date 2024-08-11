from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register_view(request):
    user_form = UserCreationForm()
    return render(
        request,
        'login.html',
        {'user_form': user_form}
    )