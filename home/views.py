from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class registerUser(View):
    def get(self, request):
        context = {"rF":registerForm}
        return render(request, 'home/register.html', context)
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['username']

        user = User.objects.create_user(username, email,password)
        user.save()

        return HttpResponse("Thành công")

class loginUser(View):
    def get(self, request):
        context = {"login":loginForm}
        return render(request, "home/login.html", context)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['username']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return render(request, "home/home.html")
        else:
            return redirect("home:home")      
           
def logoutUser(request):
    logout(request)
    return redirect("home:home")

def home(request):
    return render(request, "home/home.html")

class privatePage(LoginRequiredMixin, View):
    login_url = "/login/"
    def get(self, request):
        return render(request, "home/private.html")