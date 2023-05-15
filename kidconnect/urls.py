from django.contrib import admin
from django.urls import path
from kidconnect import views
from .views import post_region

urlpatterns = [
        path('', views.home),
        path('index', views.home),
        path('menu', views.menu),
        path('alumno', views.alumno),
        path('evento', views.evento),
        path('docente', views.docente),
        path('correo', views.correo),
        path('llamar-endpoint/', views.llamar_endpoint, name='llamar_endpoint'),
        path('post-region/', post_region, name='post_region')
        ]
