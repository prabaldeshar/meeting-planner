from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime
# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html")

def date(request):
    return HttpResponse("This page was serverd at " + str(datetime.now()))

def about(request):
    return HttpResponse("This is the about page")