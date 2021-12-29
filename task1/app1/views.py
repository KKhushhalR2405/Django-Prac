from django.shortcuts import render

# Create your views here.

def app1page1(request):
    return render(request,'app1/page1.html')

def app1page2(request):
    return render(request,'app1/page2.html')

def home(request):
    return render(request,'app1/home.html')