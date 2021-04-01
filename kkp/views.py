from django.shortcuts import render
from .models import Registration
from django.http import HttpResponse

def index(request):

    dests = Registration.objects.all()

    return render(request, 'index.html', {'dests': dests})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def icons(request):
    return render(request, 'icons.html')

def mens(request):
    return render(request, 'mens.html')

def single(request):
    return render(request, 'single.html')

def typography(request):
    return render(request, 'typography.html')

def womens(request):
    return render(request, 'womens.html')

