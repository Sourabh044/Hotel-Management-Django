from django.urls import path
from . import views

urlpatterns = [
    path('Signup/', views.Signup),
    path('ForgotPassword/', views.ForgotPassword),
    path('login/', views.userLogin),
    path('logout/', views.userlogout),
    path('changepassword/', views.changepassword),
]