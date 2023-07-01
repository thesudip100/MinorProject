from django.shortcuts import render,redirect,HttpResponse
from .forms import userRegisterForm
from django.contrib.auth import authenticate,login,logout
from home.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def customer_register(request):
        form = userRegisterForm()
        if request.method == 'POST':
            #image = request.FILES.get('c_image')
            form = userRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse(' Register SUCCESS')
        return render(request, 'user_register.html',{'form':form})

def prof_register(request):
        form = userRegisterForm()
        if request.method == 'POST':
            #image = request.FILES.get('c_image')
            form = userRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse(' Register SUCCESS')
        return render(request, 'prof_register.html',{'form':form})


def loginPage(request):
     if request.method == 'POST':
          userName=request.POST.get('username')
          passWord=request.POST.get('password')

          user=authenticate(request,username=userName,password=passWord)
          
          if user is not None:
               login(request,user)
               return HttpResponse("You're  welcomed.")
               
          else:
               return HttpResponse('You are not welcome')
          
          
     
     return render(request, 'login.html')

