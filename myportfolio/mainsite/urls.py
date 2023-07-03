from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("proyect1/", views.proyect1, name="proyect1"),
    path("admin/", admin.site.urls),
]