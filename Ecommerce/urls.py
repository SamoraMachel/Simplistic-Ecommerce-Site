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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from mainApp.views import MainPage, login_user, register_user, render_mainpage, get_specific_item, purchase_item, sales, finish_shopping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name="homepage.html"), name="home"),
    path('jambo', TemplateView.as_view(template_name="What'sup.html"), name="jambo"),
    path('about', TemplateView.as_view(template_name="aboutus.html"), name="about"),
    path('contact', TemplateView.as_view(template_name="contactus.html"), name="contact"),
    
    
    path('login', login_user, name="user"),
    path('register', register_user, name="register"),
    
    path('mainPage', render_mainpage, name="userpage"),
    path('mainPage:filtered', get_specific_item, name="filterProducts"),
    path('basktet', sales, name="basket"),
    
    path('addToCart', purchase_item, name="addToCart"),
    path('finish', finish_shopping, name="finish_shopping")
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)