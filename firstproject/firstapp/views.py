from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("First Manouna App")
    # return HttpResponse(include('firstapp.home-page.html')) #deprecated
    # return render(None, 'firstapp/home-page.html') #mesh naf3a
