from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .login_forms import LoginForm
from django.contrib.auth.decorators import login_required
from .profile_forms import ProfileForm

def home(request):
    return render(request, "accounts/home.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {
        "form": form
    })

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = LoginForm(request)

    return render(request, "accounts/login.html", {
        "form": form
    })
def user_logout(request):
    logout(request)
    return redirect("home")


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form}
    )