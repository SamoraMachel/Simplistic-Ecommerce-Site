from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import  authenticate, login

from .forms import LoginForm, RegistrationForm, ProductType
from .models import Product, ProductType, Purchase

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

def get_specific_item(request):
    if request.method == "POST":
        
        if request.POST['productType'] == 'all':   
            products = Product.objects.all()
        else:
            productType = ProductType.objects.filter(type=request.POST['productType'])
            products = Product.objects.filter(type=productType[0].id)  
            
        if request.user.is_authenticated:
            username = request.user.username
            email = request.user.email
            
            return render(request, 'userpage.html', {'username': username, 'email':email, "products":products})
    return HttpResponseRedirect("/mainPage")


def purchase_item(request):
    if request.method == "POST":
        productID = request.POST['productID']
        return HttpResponse(productID)
        # product = Product.objects.get(id=1)
        # Purchase.create(request.user, product, 1)
        
    return redirect('userpage')

def sales(request):
    if request.method == 'POST':
        itemID = request.POST['productID']
        Purchase.objects.filter(id=itemID).delete()
    user_purchases = Purchase.objects.filter(user=request.user)
    items_not_bought = user_purchases.filter(bought=False)
    return render(request, 'sales.html', {'items':items_not_bought  })

def finish_shopping(request):
    user_purchases = Purchase.objects.filter(user=request.user)
    items_not_bought = user_purchases.filter(bought=False).update(bought=True)
    return redirect('userpage')
    