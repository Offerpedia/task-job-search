from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response 
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

class LogoutView(TemplateView):
    def post(self, request):
        try:
            logout(request.user)

        except:
            return render(request, 'users/login.html')

class LoginView(TemplateView):
    template_name = 'users/login.html'
    def get(self, request): 
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('jobs:application-job-list')
            return redirect('jobs:job-list')
    def post(self, request):
        
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            print(username, password)

            if not username or not password:
                raise ValueError("Username and password are required")

            user = authenticate(username=username, password=password)

            if user is None:
                raise ValueError("Authentication failed")

        except:
            return render(request, 'users/login.html')

        if user is not None:
            login(request, user)
            if hasattr(user, 'is_staff') and user.is_staff:
                return redirect('jobs:application-job-list')
            else:
                return redirect('jobs:job-list')
        else:
            messages.error(request, "Invalid credentials")

def register_company(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        company_name = request.POST.get('company_name')
        bio = request.POST.get('bio')
        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = True
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('users:login')
        except Exception as e:
            return render(request, 'users/register_company.html')
    return render(request, 'users/register_company.html')


def register_candidate(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('users:login')
        except Exception as e:
            return render(request, 'users/register_candidate.html')
    return render(request, 'users/register_candidate.html')


