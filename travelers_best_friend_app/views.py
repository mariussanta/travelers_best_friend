from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('<h1>Travel\'s best friend!</h1>')
