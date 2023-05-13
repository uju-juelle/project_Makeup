from django.shortcuts import render
from .models import *
# Create your views here.

def home_page(request):
    kits = cosmetics.objects.all()
    return render(request, "Content/home.html", {"list_of_makeup": kits})


def about_page(request):
    return render(request, "Content/about.html")