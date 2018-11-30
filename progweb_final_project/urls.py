"""progweb_final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from book_app.views.LoginView import LoginView
from book_app.views.RegisterView import RegisterView
from book_app.views.LogoutView import LogoutView
from book_app.views.HomeView import HomeView
from book_app.views.SearchView import SearchView
from book_app.views.BookView import BookView
from book_app.views.IndexView import IndexView

from book_app.views.SearchAPI import SearchAPI
from book_app.views.WeatherAPI import WeatherAPI

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('book/', BookView.as_view(), name='book'),
    path('home/', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),

    path('search/book/', SearchAPI.as_view(), name='search'),
    path('weather/get/', WeatherAPI.as_view(), name='weather'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

