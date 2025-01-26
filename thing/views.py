from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Homework
from .models import PhotoBeforeAfter
import datetime
from random import randint

def successful(request):
    most_recent_HW = Homework.objects.order_by("-date")
    total = Homework.objects.count()
    # most_recent_HW[0].delete()

    return render(request, "thing/successful.html")

def goguardianbypass(request):
    return render(request, "thing/ggBypass.html")

def projects(request):
    return render(request, "thing/projects.html")

def cats(request):
    return render(request, "thing/cat.html")

def photos(request):
    return render(request, "thing/photos.html")

def wild(request):
    photo_list = PhotoBeforeAfter.objects.filter(event="").order_by("-date")
    context = {
            "photo_list": photo_list,
    }
    return render(request, "thing/wild.html", context)

def nyias(request):
    photo_list = PhotoBeforeAfter.objects.filter(event="nyias").order_by("-date")
    context = {
            "photo_list": photo_list,
    }
    return render(request, "thing/nyias.html", context)


# Create your views here.
def homework(request):
    latest_homework_list = Homework.objects.order_by("-date")
    funny_captions = [
        "Days Worth of Hell Saved", 
        "Days of Humiliation Saved",
        "Days of Homework Saved",]
    cnt = str(Homework.objects.count()) + " " + funny_captions[randint(0, len(funny_captions)-1)]
    context = {
        "latest_homework_list": latest_homework_list,
        "cnt": cnt,
    }
    if request.method == "POST":
        ela = request.POST.get('e')
        math = request.POST.get('math')
        science = request.POST.get('science')
        socialStudies = request.POST.get('socialStudies')
        band = request.POST.get('band')
        homeRoom = request.POST.get('homeRoom')
        pe = request.POST.get('pe')
        foreignLang = request.POST.get('foreignLang')
        misc = request.POST.get('mis')
        pwd = request.POST.get('pwd')
        if(pwd == 'NoobAtAllGames123!'): 
            Homework.objects.create(date=datetime.date.today(), ELA=ela, Math=math, Science=science, SocialStudies=socialStudies, Band=band, HomeRoom=homeRoom, PE=pe, ForeignLang=foreignLang, Misc=misc)
            return redirect(successful)
        else:
            return redirect(successful)

    return render(request, "thing/homework.html", context)

def home(request):
    return render(request, "thing/home.html")

def edit(request, num):
    cnt = Homework.objects.count()
    hw = Homework.objects.get(id=num)
    context = {
        "cnt": cnt,
        "math": hw.Math,
        "ela": hw.ELA,
        "science": hw.Science,
        "socialStudies": hw.SocialStudies,
        "band": hw.Band,
        "homeRoom": hw.HomeRoom,
        "pe": hw.PE,
        "foreignLang": hw.ForeignLang,
        "misc": hw.Misc,
    }
    if request.method == "POST":
        ela = request.POST.get('e')
        math = request.POST.get('math')
        science = request.POST.get('science')
        socialStudies = request.POST.get('socialStudies')
        band = request.POST.get('band')
        homeRoom = request.POST.get('homeRoom')
        pe = request.POST.get('pe')
        foreignLang = request.POST.get('foreignLang')
        misc = request.POST.get('mis')
        pwd = request.POST.get('pwd')
        hw = Homework.objects.get(id=num)
        hw.ELA = ela
        hw.Math = math
        hw.Science = science
        hw.SocialStudies = socialStudies
        hw.Band = band
        hw.HomeRoom = homeRoom
        hw.PE = pe
        hw.ForeignLang = foreignLang
        hw.Misc = misc
        if(pwd == 'NoobAtAllGames123!'):
            hw.save()
            return redirect(successful)
        else:
            return redirect(successful)

    return render(request, "thing/editHomework.html", context)
