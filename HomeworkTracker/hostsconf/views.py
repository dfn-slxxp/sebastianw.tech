from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render(request, "saraellyticket/home.html")

def why(request):
    return render(request, "saraellyticket/why.html")

def about(request):
    return render(request, "saraellyticket/about.html")

def mission(request):
    return render(request, "saraellyticket/mission.html")

def contact(request):
    return render(request, "saraellyticket/contact.html")

def events(request):
    return render(request, "saraellyticket/events.html")

def transparency(request):
    return render(request, "saraellyticket/transparency.html")
