from django.urls import path
from django.conf import settings
from . import views
from . import templates 
from django.urls.conf import include
from django.conf.urls.static import static

urlpatterns = [
    path('', views.hotelviews),
    # path('', views.hotelviews),
    path('Hotels/', views.Hotels),
    path('Welcome/', views.welcome, name="Welcome page"),
    path('Aboutus/', views.aboutus, name="About Us" ),
    path('Contactus/', views.contactus, name="Contact Us" ),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)