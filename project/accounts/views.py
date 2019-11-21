from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form,}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
        
    else:
        form = AuthenticationForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('movies:index')


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {'person': person,}
    return render(request, 'accounts/profile.html', context)


@login_required
def follow(request, username, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    user = request.user

    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
        else:
            person.followers.add(user)
        
    return redirect('accounts:profile', username)
