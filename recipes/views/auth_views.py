import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.urls import reverse
from django.conf import settings
from recipes.models import User

def login_view(request):
    """Login page"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "recipes/login.html", {"message": "Invalid username and/or password."})

    return render(request, "recipes/login.html")


def logout_view(request):
    """Logs the user out and redirects to the index page"""
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register_view(request):
    """Allows the user to create an account"""
    if not settings.DEBUG:
        return render(request, "recipes/register.html", {"message": "Registration deactivated."})

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "recipes/register.html", {"message": "Passwords must match."})

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "recipes/register.html", {"message": "Username already taken."})

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "recipes/register.html")
