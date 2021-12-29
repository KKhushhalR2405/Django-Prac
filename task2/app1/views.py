from django.shortcuts import render,HttpResponse
from .models import User
# Create your views here.


def index(request):
    allnames = User.objects.all()
    content = {
        'details': allnames,
    }
    return render(request, 'index.html',context = content)