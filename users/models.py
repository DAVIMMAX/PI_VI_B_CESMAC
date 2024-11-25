from django.db import models
from django.contrib.auth.models  import User
from datetime import date



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True, default=date.today)
    cpf = models.CharField( max_length=14, blank=True, null=True)



    def __str__(self) -> str:
        return f'perfil de {self.user.username}'
