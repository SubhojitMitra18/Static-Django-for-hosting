from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    student=[
        {'name':'Dipan Dutta','marks':20},
        {'name':'Debraj Malakar','marks':19},
        {'name':'Aditi Roy','marks':20},
        {'name':'Aman Kumar','marks':20},
    ]
    return render(request,'index.html',context={'student':student})

def about(request):
    return render(request,'about.html')