from django.contrib import admin
from django.db.models.base import Model
from about_us.models import about_us_logo, About_Us, Team_about
from django.contrib.admin.options import ModelAdmin

# Register your models here.

class About_UsAdmin(ModelAdmin):
    list_display = ["about_img", "about_title", "about_disc", "about_intg", ]

class Team_aboutAdmin(ModelAdmin):
    list_display = ["team_img", "team_name", "team_about"]


class about_us_logoAdmin(ModelAdmin):
    list_display = ["logo_img"]


admin.site.register(about_us_logo,about_us_logoAdmin)
admin.site.register(About_Us,About_UsAdmin)
admin.site.register(Team_about,Team_aboutAdmin)