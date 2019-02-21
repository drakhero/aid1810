from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("index的index")

def login(request):
    return HttpResponse('index的login')

def register(request):
    return HttpResponse('index的register')