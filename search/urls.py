from django.urls import path
from . import views
from search.views import SearchViews

urlpatterns = [
    path('', SearchViews.as_view(), name='search')
]
