from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegistroUsuario.as_view(), name='register'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('agregar_superheroe/', views.agregar_superheroe, name='agregar_superheroe'),
]