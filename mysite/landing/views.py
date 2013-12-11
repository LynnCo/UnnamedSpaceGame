import os
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    url = "landing/static/landing/story.txt"
    with open(url,"r") as story:
        content = story.readlines()
    content = [line.strip() for line in content]
    err = "none"
    return render(request,"landing/index.html", {"words":content[0],"err":err})
def test(request,inp):
    return HttpResponse("Your input was %s" %(inp))
def empty(request):
    return HttpResponse("Test successful!")