from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello My Name is Shakil")


def show_patern(request):
    return HttpResponse("Hello World !")

def show_specific_task(request,id):
    print("Urls id is a ",id)
    print(type(id))
    return HttpResponse(f"Hello this is a Dynamic Urls id is {id}")