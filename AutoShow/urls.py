"""AutoShow URL Configuration

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
from Autos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('Autos/list/', MostrarAuto.as_view(), name="auto-list"),
    path('Autos/<pk>/detail', AutoDetail.as_view(), name="auto-detail"),
    path('Autos/create', AutoCreate.as_view(), name="auto-create"),
    path('Autos/<pk>/update', AutoUpdate.as_view(), name="auto-update"),
    path('Autos/<pk>/delete', AutoDelete.as_view(), name="auto-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', LogIn.as_view(), name="login"),
]