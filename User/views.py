from django.shortcuts import render
from django.http import HttpResponse

def forgotPassword(request):
    return render(request, 'Forgot Password.html')

def Signup(request):
    return render(request, 'Signup.html')

def Login(request):
    return render(request, 'login/login.html')
