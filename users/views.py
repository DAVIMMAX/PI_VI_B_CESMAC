from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.models  import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from posts.models import Post

# Create your views here.

class Cadastro(CreateView):
    model = User
    form_class = UserRegistrationForm  # Certifique-se de que UserRegistrationForm está correto
    template_name = 'cadastro.html'
    success_url = reverse_lazy('profile-update')

    def form_valid(self, form):
        user = form.save()  # A senha será criptografada automaticamente
        Profile.objects.create(user=user)  # Criação do perfil
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-update', kwargs={'pk': self.object.profile.pk})
    

class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'perfil.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        perfil = get_object_or_404(Profile, user=user)
        return perfil

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(profile=self.object).order_by('-data')
        return context

class HomeView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'home.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        try:
            
            profile = self.request.user.profile  
        except Profile.DoesNotExist:
            raise Http404("Não existe perfil associado a este usuário.")
        
        return profile
    

    
    """    
    def get_object(self, queryset=None):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        perfil = get_object_or_404(Profile, user=user)
        return perfil
        
        """

"""
    def get_object(self, queryset=None):
        profile = super().get_object(queryset)
        if profile.user != self.request.user:
            raise Http404("Você não tem permissão para acessar este perfil.")
        return profile
"""