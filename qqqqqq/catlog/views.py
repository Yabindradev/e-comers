
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import ProductsFrom, CategoryForm, CustomerForm
from .models import *

def home(request):
    return render(request, 'pages/home.html')
# -------------------user authenticate section-------------------
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            messages.info(request, "Username and password are invalid")
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def singup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username  alreadt exist")
                return redirect('singup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email address is already registered")
                return redirect('singup')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password is invalid")
            return redirect('singup')
    else:
        return render(request, 'pages/singup.html')


def logout(request):
    auth_logout(request)
    return redirect('main')

# ----------------user authenticate end section------------------


# -----------ecomers pages section --------------------------------

# def main(request):
#     products = Product.objects.all()
#     return render(request, "pages/main.html", {'products':products})


def product_list(request):
    queryset = Product.objects.all()  # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "pages/product_list.html", context)


def product_detail(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "pages/product_detail.html", context)



def help(request):
    return render(request, 'pages/help.html')


def sell(request):
        pforms = ProductsFrom(request.POST)
        if pforms.is_valid():
            pforms.save()
            return redirect('/')
            
            
        return render(request, 'pages/sell.html', {'pforms':pforms})
    
# -----------ecomers pages section --------------------------------



# -------------------dashbord section------------------------------

def dmain(request):
    return render(request, 'pages/dmain.html')


# @login_required
def dashbord(request):
    return render(request, 'pages/dashbord.html')



def products(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products': products})


def create(request):
     pforms = ProductsFrom()
     if request.POST:
         forms = ProductsFrom(request.POST)
         if forms.is_valid():
             forms.save()
             return redirect('dashbord')
     return render(request, 'pages/create.html', {'pforms': pforms})
 

def category(request):
    cform = CategoryForm()
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('dashbord')
    return render(request, 'pages/category.html', {'cform': cform})

# -------------------dashbord end------------------------------



# --------------------user informaction------------------------
def user_informaction(request):
    user_address = CustomerForm()
    if request.POST:
        user_address = CustomerForm(request.POST)
        if user_address.is_valid():
            user_address.save()
            return redirect('/')
    return render (request, 'pages/user_profile.html', {'user_address':user_address})


def overview(request):
    return render(request, 'user/overviews.html')

# def product_list_view(request):
#     queryset = Product.objects.all()  # list of objects
#     return render(request, "products/product_list.html", {'queryset': queryset})


# def detail(request, id):
#     obj = get_object_or_404(Product, id = id)
#     return render(request, 'pages/detail.html')
