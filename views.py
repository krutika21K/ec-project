from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth

# Create your views here.

def account(request):
    return render(request,'account.html')
   
def cart(request):
    return render(request,'cart.html')