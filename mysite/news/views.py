from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls news index.")

def index123(request):
    return HttpResponse("Hello, world. You're at the polls news index123.")