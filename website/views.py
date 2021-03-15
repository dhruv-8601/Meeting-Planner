from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datetime_safe import datetime

from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

# Please add: An about page that shows some text about yourself
def about(request):
    return HttpResponse("I'm Dhruv and I learn courses from Pluralsight.")
