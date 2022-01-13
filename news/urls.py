from django.urls import path
from . import views


urlpatterns = [

    path('', views.BlogPage.as_view(), name='blog'),
    path('/<int:id>/<str:slug>/', views.PostDetail.as_view(), name='post')
   
]
