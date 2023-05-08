from django.contrib import admin
from django.urls import path
from kidconnect import views

urlpatterns = [
        path('', views.home),
        path('index', views.home),
        path('menu', views.menu),
        path('alumno', views.alumno),
        path('llamar-endpoint/', views.llamar_endpoint, name='llamar_endpoint'),
        ]
