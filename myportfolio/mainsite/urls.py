from django.contrib import admin
from django.urls import include, path
import project1
import project2
import project3
import project4
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("project1/", include("project1.urls")),
    path("project2/", include("project2.urls")),
    path("project3/", include("project3.urls")),
    path("QR-extractor/", include("project4.urls")),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()