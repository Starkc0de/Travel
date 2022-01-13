from django.urls import path
from services.views import Service


urlpatterns = [

    path('', Service.as_view(), name='services_us')
]
