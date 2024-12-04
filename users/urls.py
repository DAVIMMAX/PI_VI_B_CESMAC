from django.contrib import admin
from django.urls import include, path
from users import views
from .views import Cadastro, ProfileUpdateView, ProfileView, HomeView
from posts import urls as postsUrls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    path('cadastro/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/<int:pk>/',  ProfileView.as_view(), name='profile-user'),
    path('home/<int:pk>/', HomeView.as_view(), name='home'),
    path('home/denuncias/<int:pk>/', postsUrls.PostListView.as_view(), name='post-list'),
    path('users/home/denuncias/', include('posts.urls'))
    
]
