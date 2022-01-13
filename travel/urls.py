"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('contact_us', include(
        ('contact_us.urls', 'contact_us'), namespace='contact_us')),
    path('about_us', include(('about_us.urls', 'about_us'), namespace='about_us')),
    path('services', include(('services.urls', 'services'), namespace='services')),
    path('blog', include(('news.urls', 'blog'), namespace='blogs')),
    path('destination', include(
        ('destination.urls', 'destination'), namespace='destination')),
    path('accounts', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('search', include(('search.urls', 'search'), namespace='searchs')),
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here

]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
