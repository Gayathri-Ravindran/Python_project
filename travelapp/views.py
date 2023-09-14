from django.http import HttpResponse
from django.shortcuts import render
from .models import Payment, Place  # Import your models here

def demo(request):
    dem = Payment.objects.all()
    var = Place.objects.all()
    return render(request, "index.html", {'res': dem, 'key': var})

     #return HttpResponse("Hello World")
     #return render(request, "home.html")
# def index(request):
