from django.shortcuts import render

from django.http import HttpResponse
def index(reguest):
    return HttpResponse("Twoj pierwszy widok. Wstep do ankiety")


# Create your views here.
