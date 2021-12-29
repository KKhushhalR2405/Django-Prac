from django.shortcuts import render

# Create your views here.

def app2page1(request):
    return render(request,'app2/page1.html')