from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import viewsets
from .models import User, Field, Update
from .serializers import UserSerializer, FieldSerializer, UpdateSerializer
from django.contrib.auth.models import User

#Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # make sure this URL exists
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

#Signup 
def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

          # confirms if a user exists 
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("signup")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        
        messages.success(request, "Account created successfully!")

        return redirect("/login/")

    return render(request, "signup.html")



def login_page(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def fields_page(request):
    return render(request, "fields.html")

def crops_page(request):
    return render(request, "crops.html")




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class UpdateViewSet(viewsets.ModelViewSet):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer

