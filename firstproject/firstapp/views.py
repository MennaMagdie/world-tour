from django.shortcuts import render
from .models import Tour
# from django.http import HttpResponse

# Create your views here.
def index(request):
    tours = Tour.objects.all() #storing all objects that are instances of Tour Class

    context = {'tours':tours}


    # return HttpResponse("First Manouna App") #rendering a string
    # return HttpResponse(include('firstapp.home-page.html')) #deprecated
    # return render(request, 'tours/index.html')
    return render(request, 'tours/index.html', context)
