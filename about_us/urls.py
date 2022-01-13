from django.urls import path

from about_us.views import AboutPage

urlpatterns = [

    path('', AboutPage.as_view(), name='AboutUs')
]
