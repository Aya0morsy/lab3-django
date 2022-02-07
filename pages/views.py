
from email import message
from multiprocessing import context
import re
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import myuser1,track as track1,add_trainee2
from django.contrib.auth import authenticate,login as authlogin,logout as auth_logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def home(request):
   return render(request,'pages/home.html')


def contact(request):
 return render(request,'pages/contact.html')


def about(request):
 return render(request,'pages/about.html')


def register(request):
    myuser11=myuser1()
    myuser12=User()
    context={};
    context['id']=1

    if(request.method=='POST') :
       name=request.POST['uname']
       password=request.POST['psw']
       myuser11.name=name
       myuser11.password=password
       User.objects.create_user(username=name,password=password,is_staff=True)

    myuser11.save()
   
    
    render(request,'pages/login.html')

    if myuser11.name=="" or myuser11.password=="":
     context['message']='empty feild'
    
     
    return render(request,'pages/register.html',context)  

def login(request):
   return render(request,'pages/login.html')

def checklogin(request):
   
   if request.method=='POST':
      username=request.POST['uname']
      passw=request.POST['psw']
      user=myuser1.empAuth_objects.all().filter(name=request.POST['uname'],password=request.POST['psw'])
      authuser=authenticate(request,username=username,password=passw)
      if(len(user)>0 and authuser is not None):
             request.session['uname']=request.POST['uname']
             authlogin(request,authuser)
             return redirect('home')
          
   else:
      return redirect(login)         

      
def logout(request):
         request.session.clear
         auth_logout(request)
         return render(request,'pages/login.html')





def addtrack(request):
   track11=track1()
   if(request.method=='POST') :
     context={};
     context['id']=1
     
     trackname=request.POST['trname']
     track11.track_name=trackname 
     track11.save()
   return render(request,'pages/addtrack.html')  




def addtrainee(request):
   track99=track1()
   trainee=add_trainee2()
   if(request.method=='POST') :
     context={};
     context['id']=1
     traineename=request.POST['traineeName']
     fac=request.POST['Fname']
     trac=request.POST['Tname']
     trainee.trainee_name=traineename
     trainee.faculty=fac
     trainee.track=track1.objects.get(id=request.POST['Tname'])
     trainee.save()
    
 
   return render(request,'pages/addtrainee.html')  

def index(request):
   trainees=add_trainee2.objects.all()
   return render(request,'pages/trainee.html',{'trainees':trainees})

def track111(request):
   track12=track1.objects.all()
   return render(request,'pages/track.html',{'tracks':track12})

def update(request,id):
     trainees=add_trainee2.objects.get(id=id)
     return render(request,'pages/update.html',{'trainees':trainees})

def actupdate(request,id):
   traineee=add_trainee2.objects.get(id=id)
   traineee.trainee_name=request.POST['trainee_name']
   traineee.faculty=request.POST['faculty']
   traineee.track=track1.objects.get(id=id)
   traineee.save()
   return redirect('/')


def dell(request,id):
     traineee=add_trainee2.objects.get(id=id)
     traineee.delete()
     return render(request,'pages/trainee.html')

