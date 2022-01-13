from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import news_logo
from .models import Blogpost

# Register your models here.
class BlogpostAdmin(ModelAdmin):
    list_display = ["postimg", "auther",
                    "title", "blog", "postdatetime","slug" ]

class news_logoAdmin(ModelAdmin):
    list_display = ["logo_img"]


admin.site.register(news_logo, news_logoAdmin)
admin.site.register(Blogpost, BlogpostAdmin)
