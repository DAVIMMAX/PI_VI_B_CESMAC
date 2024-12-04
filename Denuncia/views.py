from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home', kwargs={'pk':self.request.user.pk})
    
def custom_logou_view(request):
    logout(request)
    return redirect('/')