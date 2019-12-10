from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'basic/index.html', {})

def blog(request):
    return render(request, 'basic/blog.html', {})

def mentor(request):
    return render(request, 'basic/mentor.html', {})

def mentee(request):
    return render(request, 'basic/mentee.html', {})

def author(request):
    return render(request, 'basic/author.html', {})
