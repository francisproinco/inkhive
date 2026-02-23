from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "auth/login.html")


ddef register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not password:
            return render(request, "auth/register.html", {
                "error": "All fields required"
            })

        if User.objects.filter(username=username).exists():
            return render(request, "auth/register.html", {
                "error": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "auth/register.html")
