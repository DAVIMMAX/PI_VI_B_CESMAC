from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label='Senha'
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['telefone', 'data_nascimento', 'cpf']
