from builtins import print
from django.conf import settings
from django.db import models
from django.http.response import HttpResponse
from django.views import generic 
from django.views.generic import ListView
from django.shortcuts import render
# Create your views here.
from about_us.models import about_us_logo
from contact_us.models import contact_us_logo
from services.models import Service_logo
from home.models import HomePageModel, home_logo, home_des
from django.template.defaulttags import register
from news.models import news_logo



class HomePage(generic.TemplateView, ListView):
    model = HomePageModel
    template_name = "index.html"
    ordering = ['id']
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        data = HomePageModel.objects.all()
        get_des = home_des.objects.all()

        page_name = "Home"
        return render(request, self.template_name, {'get_des': get_des, 'data': data, 'page_name': page_name})


@register.filter(name='get_logo')
def get_logo(demo):

    if 'Home' == demo:
        if home_logo.objects.all().exists():
            get_data = home_logo.objects.all().first()
            if get_data.logo_img:
                logo_image = get_data.logo_img.url
        return str(logo_image)

    elif 'ContactUs' == demo:
        if contact_us_logo.objects.all().exists():
            get_data = contact_us_logo.objects.all().first()
            if get_data.logo_img:
                logo_image = get_data.logo_img.url
        return str(logo_image)

    elif 'AboutUs' == demo:
        if about_us_logo.objects.all().exists():
            get_data = about_us_logo.objects.all().first()
            if get_data.logo_img:
                logo_image = get_data.logo_img.url
        return str(logo_image)

    elif 'news' == demo:
        if news_logo.objects.all().exists():
            get_data = news_logo.objects.all().first()
            if get_data.logo_img:
                logo_image = get_data.logo_img.url
        return str(logo_image)

    elif 'services' == demo:
        if Service_logo.objects.all().exists():
            get_data = Service_logo.objects.all().first()
            if get_data.logo_img:
                logo_image = get_data.logo_img.url
        return str(logo_image)
