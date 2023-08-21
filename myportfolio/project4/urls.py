from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("QR-extractor/", views.project4, name="project4main"),
    path("success/", views.upload_file, name="upload"),
   
    
]