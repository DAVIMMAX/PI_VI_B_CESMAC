"""
URL configuration for Denuncia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from .views import CustomLoginView, custom_logou_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/',  custom_logou_view, name='logout'),
    path('users/',  include('users.urls')),
    path('', CustomLoginView.as_view(), name='index')

]

if settings.DEBUG: #prestar atenção! faz com que o arquivo seja servido mesmo em ambiente de desenvolvimento.  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)