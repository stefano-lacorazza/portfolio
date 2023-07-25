from django.contrib import admin
from location_field.models.plain import PlainLocationField

from .models import Place

admin.site.register(Place)