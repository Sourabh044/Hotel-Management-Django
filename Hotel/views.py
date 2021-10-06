from django.shortcuts import render
from django.http import HttpResponse
from .models import hotel

def welcome(request):
    return HttpResponse("<h1> Welcome User! <h1/>")

def hotelviews(request):
    allhotel = hotel.objects.all()
    return render(request, 'MAIN.html', {'hoteldata':allhotel})

def aboutus(request):
    return render(request, 'about us/about us page.html')

def contactus(request):
    return render(request, 'contact us/contact us.html')