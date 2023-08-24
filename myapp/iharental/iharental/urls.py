"""
URL configuration for iharental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from iha.views import index, rent, release
from user_operations.views import login, sign_up, logout

urlpatterns = [
    path('', login, name='login'),
    path('', logout, name='logout'),
    path('sign_up/', sign_up, name='sign_up'),
    path('index/', index, name='index'),
    path('<int:iha_id>/rent/', rent, name='rent'),
    path('<int:iha_id>/release/', release, name='release'),
    path('admin/', admin.site.urls),
]
