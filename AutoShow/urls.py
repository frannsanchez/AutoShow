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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('Autos/about', about, name="about"),
    path('Autos/list/', MostrarAuto.as_view(), name="auto-list"),
    path('Autos/search', BuscarAuto, name="auto-search"),
    path('Autos/<pk>/detail', AutoDetail.as_view(), name="auto-detail"),
    path('Autos/create', AutoCreate.as_view(), name="auto-create"),
    path('Autos/<pk>/update', AutoUpdate.as_view(), name="auto-update"),
    path('Autos/<pk>/delete', AutoDelete.as_view(), name="auto-delete"),
    path('Mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('Mensaje/list/', MostrarMensaje.as_view(), name="mensaje-list"),
    path('Mensaje/<pk>/detail', MensajeDetail.as_view(), name="mensaje-detail"),
    path('Mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', LogIn.as_view(), name="login"),
    path('logout/', LogOut.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('profile/<pk>/detail', ProfileDetail.as_view(), name="profile-detail"),
    path('profile/create', ProfileCreate.as_view(), name="profile-create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
