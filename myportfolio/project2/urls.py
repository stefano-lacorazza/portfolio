from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path("", views.project2, name="project2main"),
   
    
]