from django.urls import path
from . import views

app_name = 'inicio_ortiz'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ciberseguridad/', views.ciberseguridad, name='ciberseguridad'),
    path('videojuegos/', views.videojuegos, name='videojuegos'),
]