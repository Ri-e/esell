from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import createForm, createCats
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

def index(request):
    
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    products = Product.objects.filter(Q(category__category__icontains=q) | Q(user__username__icontains=q) | Q(brand__icontains=q) | Q(modelname__icontains=q) | Q(opertingsys__icontains=q) | Q(cellulartech__icontains=q) ).order_by('-created') 
    category = Category.objects.all()
    return render(request, "library/home.html",{'products' : products, 'category':category})

def product(request, pk):
    product = Product.objects.get(id=pk)
    buyers = product.buyers.count()

    return render(request, "library/product.html", {'product' : product, 'buyers' : buyers})
def create(request):
    form = createForm()
    if request.method == 'POST':
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('home')
    return render(request, 'library/create.html', {'form' : form})

def loginPage(request):
    page='login'
    # u cant enter login page if already logged in
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            # u cant log in if not registered
            user = User.objects.get(username=username)
        except:

            messages.error(request, "User does not exist")
        # authentication stuff
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")
    return render(request, 'library/login_register.html', {'page' : page})


def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Something went error")
    return render(request, 'library/login_register.html', {'form' : form})
    
def delete(request, pk):
    product= Product.objects.get(id=pk)
    if request.user != product.user:
        return redirect('home') 
    if request.method == "POST":
        product.delete()
        return redirect('home')
        
    return render(request, 'library/delete.html')
def update(request, pk):
    product = Product.objects.get(id=pk)
    if request.user != product.user:
        return redirect('home') 

    form = createForm(instance=product)
    if request.method == "POST":
        form =  createForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product', product.id)
    return render(request, 'library/create.html', {'form' : form})
def createCat(request):
    form = createCats()
    if request.method == 'POST':
        form = createCats(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'library/createCat.html', {'form' : form})