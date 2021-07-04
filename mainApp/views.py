from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import  authenticate, login

from .forms import LoginForm, RegistrationForm
from .models import Product

# Create your views 

class MainPage(LoginRequiredMixin, TemplateView):
    template_name = "userpage.html"
    login_url = "/login"
    

def login_user(request):
    if request.method == 'POST':
        form  = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("userpage")
            else:
                form.add_error('username',"Invalid username or password.")
                form.add_error('password',"Invalid username or password.")
        else:
            form.add_error('password', "Invalid username or password")
            form.add_error('username',"Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'user.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("userpage")
    else: 
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def render_mainpage(request):
    
    queryset = Product.objects.all()
    
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        
        
        return render(request, 'userpage.html', {'username': username, 'email':email, "products":queryset})
    return HttpResponseRedirect("/login")
    