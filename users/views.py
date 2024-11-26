from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib.auth.models  import User
from .models import Profile

# Create your views here.

class Cadastro(CreateView):
    
    
    model = User
    form_class = UserRegistrationForm
    template_name = 'cadastro.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):

        user = form.save()

        Profile.objects.create(user=user)

        return super().form_valid(form)
       
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.profile.pk})
    

class ProfileUpdateView(UpdateView):

    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile.html'
    success_url = reverse_lazy('home')