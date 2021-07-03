"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="homepage.html"), name="home"),
    path('jambo', TemplateView.as_view(template_name="What'sup.html"), name="jambo"),
    path('about', TemplateView.as_view(template_name="aboutus.html"), name="about"),
    path('contact', TemplateView.as_view(template_name="contactus.html"), name="contact"),
    
    
    path('login', TemplateView.as_view(template_name="user.html"), name="user"),
    path('register', TemplateView.as_view(template_name="register.html"), name="register"),
    
    path('mainPage', TemplateView.as_view(template_name="userpage.html"), name="userpage"),
    
] 
