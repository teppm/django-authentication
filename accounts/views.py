from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.

def index(request):
    """Return the index html file"""
    return render(request, 'index.html')


def logout(request):
    """Logout the user"""
    auth.logout(request)
    messages.success(request, 'You have been logged out Yo!')
    return redirect(reverse('index'))

