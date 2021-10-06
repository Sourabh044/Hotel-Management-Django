from django.urls import path
from . import views
from . import templates 
from django.urls.conf import include

urlpatterns = [
    path('Signup', views.Signup),
    path('ForgotPassword', views.forgotPassword),
    path('login', views.Login),
    # path('ChangePassword', views.changepassword),  
]