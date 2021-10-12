from django.shortcuts import render
from django.http import HttpResponse
from .models import hotel

def welcome(request):
    return HttpResponse("<h1> Welcome User! <h1/>")

def hotelviews(request):
    return render(request, 'MAIN.html')

def aboutus(request):
    return render(request, 'about us page.html')

def contactus(request):
    return render(request, 'contact us.html')

def Hotels(request):
    allhotel = hotel.objects.all()
    return render(request, 'HotelList.html', {'hoteldata':allhotel})

