from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from verify_email.email_handler import send_verification_email

def ForgotPassword(request):
    return render(request, 'Forgot Password.html')

def Signup(request):
    # if request method post AsyncGenerator
    #     request.post se sara data utha lena
    #     newuser = User(name = name, email = email, password=password,)
    #     newuser.save()
    #     login(request, newuser)
    #     return redirect('/')
    # return render(request, 'Signup.html')
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        newuser = User.objects.create_user(username = username , password = password, email=email)
        newuser.save()
        return redirect('/')
    else:
        # return HttpResponse('Error')
        return render(request, 'Signup.html')

def userLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Invalid User name password")
    else:
        return render(request, 'login.html')

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('user/login')

def changepassword(request):
    if request.user.is_authenticated:
            if request.method =='POST':
                user = request.user
                password = request.POST['password2']
                # get password from form
                user.set_password(password)
                user.save()
            else:
                return render(request, 'ChangePassword.html')
    elif request.user.is_authenticated:
             return render(request, 'ChangePassword.html') 
    else:
        return redirect('/')
