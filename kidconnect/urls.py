from django.contrib import admin
from django.urls import path
from kidconnect import views
from .views import post_region
from .views import login, menu, docente


urlpatterns = [
        path('', views.home),
        path('index/', login, name='index'),
        path('menu/', menu, name='menu'),
        path('docente/', docente, name='docente'),
        path('crearUsuario', views.alumno, name='crearUsuario'),
        path('evento', views.evento, name='evento'),
        path('correo', views.correo, name='correo'),
        path('llamar-endpoint/', views.llamar_endpoint, name='llamar_endpoint'),
        path('post-region/', post_region, name='post_region'),
        path('crearAlumno', views.crearAlumno, name='crearAlumno'),
        ]
