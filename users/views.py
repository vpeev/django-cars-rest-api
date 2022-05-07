from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import SignUpForm

def home(request):
    return render(request, 'users/home.html' )

def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)