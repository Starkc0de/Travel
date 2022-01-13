from django.urls import path

from accounts.views import AccountsView, SigninView

urlpatterns = [

    path('', AccountsView.as_view(), name='Account'),
    path('/signin', SigninView.as_view(), name='Signin')
]
