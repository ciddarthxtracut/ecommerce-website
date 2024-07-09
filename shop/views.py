from django.shortcuts import render

def home(request):
    return render(request,"shop/layouts/index.html")

def register(request):
    return render(request,"shop/layouts/registration.html")