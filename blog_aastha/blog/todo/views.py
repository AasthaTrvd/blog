from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    #return HttpResponse('about')
    return render(request,'about.html')

def homepage(request):
    #return HttpResponse('homepage')
    return render(request,'homepage.html')

# Create your views here.
