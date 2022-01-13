from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Service_logo, ServiceModel

# Register your models here.

class ServiceModelAdmin(ModelAdmin):
    list_display = ["img","name","title"]


class Service_logoAdmin(ModelAdmin):
    list_display = ["logo_img"]


admin.site.register(Service_logo, Service_logoAdmin),
admin.site.register(ServiceModel, ServiceModelAdmin)
