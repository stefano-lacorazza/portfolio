from django.contrib import admin
from django.urls import include, path
import project1
import project2

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("project1/", include("project1.urls")),
    path("project2/", include("project2.urls")),
    #path("project3/", include("project3.urls")),
    path("admin/", admin.site.urls),
]