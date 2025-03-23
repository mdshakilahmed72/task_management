from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello My Name is Shakil")


def show_patern(request):
    return HttpResponse("Hello World !")