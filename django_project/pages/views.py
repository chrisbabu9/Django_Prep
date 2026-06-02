from django.http import HttpResponse
from django.shortcuts import render


def home_page_view(request):
    return HttpResponse("Home Page")

def about_page_view(request):
    return render(request,"pages/about.html")