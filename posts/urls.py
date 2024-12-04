from django.urls import path
from . import views
from .views import PostListView, PostCreateView, PostDeleteView #eu sei... eu sei que poderia importar tudo da views acima, 
#mas serviu para lembrar das classes

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('cadastrar/', PostCreateView.as_view(), name='cadastrarPost'),
    path('descricao/', views.tipos_ocorrencias, name='descricao'),
    path('', views.DeleteView.as_view(), name='deletar'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
    
]

