from django.http import request
from django.shortcuts import render


# Create your views here.

def index1(request):
    return render(request,'master.html')

def index(request):
    return render(request,'index.html')

def templateFun(request):
    return render(request,'templates.html')

def personal(request):
    return render(request,'personal.html')

def experiences(request):
    return render(request,'experiences.html')