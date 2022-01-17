"""Django_KeralaTourism_Test URL Configuration

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
from kt import views
from kt.views import home

urlpatterns = [
path('', home, name='home'),
    path('admin/', admin.site.urls),
path('home/', views.home),
path('Register/', views.Register),
path('home2/', views.home2),
path('login/', views.login),
path('gallery/', views.gallery),
path('nelliyampathy/', views.nelliyampathy),
path('kovalam/', views.kovalam),
path('athirappilly/', views.athirappilly),
path('save/', views.save),
path('save1/', views.save1),
path('save2/', views.save2),
path('loginpage/', views.loginpage),
path('about/', views.about),


]
