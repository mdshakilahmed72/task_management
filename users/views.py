from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cont(request):
    return HttpResponse("Hello My Name is Django")