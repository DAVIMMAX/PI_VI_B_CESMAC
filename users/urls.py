from django.contrib import admin
from django.urls import include, path
from users import views
from .views import Cadastro, ProfileUpdateView
from Denuncia.views import home

urlpatterns = [
    path('', home),
    path('cadastro/', Cadastro.as_view()),
    path('profile/<int:pk>',  ProfileUpdateView.as_view(), name='profile'),
]