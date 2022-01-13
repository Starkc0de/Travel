from django.urls import path

from destination.views import DestinationView

urlpatterns = [

    path('/<int:id>/<str:slug>/', DestinationView.as_view(), name='DestinationView')

]
