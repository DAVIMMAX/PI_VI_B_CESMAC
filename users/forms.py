from django import forms
from django.contrib.auth.models import User
from .models import Profile

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Digite sua senha'}),
        label='Senha'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Redigite a senha'}),
        label='Confirmar senha'
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome de usuário'}),
        help_text=''
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("As senhas não coincidem.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['telefone', 'data_nascimento', 'cpf', 'picture']
