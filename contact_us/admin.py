from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from contact_us.models import Contact_Us, contact_us_logo


# Register your models here.


class Contact_UsAdmin(ModelAdmin):
    list_display = ["name", "email", "subject", "message"]


class contact_us_logoAdmin(ModelAdmin):
    list_display = ["logo_img"]


admin.site.register(Contact_Us, Contact_UsAdmin)
admin.site.register(contact_us_logo, contact_us_logoAdmin)
