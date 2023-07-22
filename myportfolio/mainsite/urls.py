from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proyect1/", views.proyect1, name="proyect1"),
    path("proyect2/", views.proyect2, name="proyect2"),
    path("proyect3/", views.proyect3, name="proyect3"),
    path("admin/", admin.site.urls),
]