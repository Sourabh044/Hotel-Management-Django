from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Hotel.urls')),
    # path('/', include('Hotel.urls')),
    path('user/', include('User.urls')),
    path('Bookings/', include('Bookings.urls')),
    path('Room/', include('Rooms.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
