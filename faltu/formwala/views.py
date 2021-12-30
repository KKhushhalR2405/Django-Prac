from django.shortcuts import render
from . import forms
# Create your views here.
def index(request):
    return render(request, 'index.html')

def view_formname(request):
    form = forms.FormName()

    if request.method=='POST':
        form = forms.FormName(request.POST)
        print(form)

    return render(request, 'formwala/form1.html', context = {'form1':form,})