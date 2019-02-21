from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show01(request):
    return HttpResponse("这是music应用中的show01")

def index(request):
    return HttpResponse("music的index")