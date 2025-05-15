from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("Code with Divyansh!")

def v1(response):
    return HttpResponse("<h1>This is my portfolio website</h1>")
