from django.contrib import admin
from .models import HomePageModel, home_logo, home_des
from django.contrib.admin.options import ModelAdmin


# Register your models here.


class HomePageModelAdmin(ModelAdmin):
    list_display = ["destination_name", "special_offer",
                    "about_destination", "destination_rate", "slug", ]


class home_logoAdmin(ModelAdmin):
    list_display = ["logo_img"]


class home_desAdmin(ModelAdmin):
    list_display = ["page_des"]


admin.site.register(HomePageModel, HomePageModelAdmin)
admin.site.register(home_logo, home_logoAdmin)
admin.site.register(home_des, home_desAdmin)
