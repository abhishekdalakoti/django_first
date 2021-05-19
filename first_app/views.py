from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>HELLO WORLD</em>")

def home(request):
    return HttpResponse("<h1>FIRST APP LANDING PAGE<h1>")
