from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")

def sex(request):
    return HttpResponse("sex")
    