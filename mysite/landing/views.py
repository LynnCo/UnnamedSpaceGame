from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {"get_food": "candy"}
    return render(request,"landing/index.html", context)
def test(request,inp):
    return HttpResponse("Your input was %s" %(inp))
def empty(request):
    return HttpResponse("Test successful!")