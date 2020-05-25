from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name ="index"),
    path('search/', views.image_search, name = "image_search"),
    path('locations/<str:location>', views.location_images, name = "locations")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)