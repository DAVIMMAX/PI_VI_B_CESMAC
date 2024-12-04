from django.db import models
from users.models import Profile

class Post(models.Model):
    type_choices = [
        ('EA','Exposição acidental'),
        ('ANA','Acessos não autorizados'),
        ('PRD','Perda ou roubo de dispositivos'),
        ('PH','Phishing(Tentativas de obter informações sensíveis)'),
        ('AES','Ataques de engenharia social'),
        ('MLW','Malware'),
        ('AIA','Acesso interno não autorizado'),
        ('OT','Outros')
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts') #models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=False, null=False,)
    typeOccurrence = models.CharField(max_length=3, choices=type_choices, default='OT')
    data = models.DateField(auto_now_add=True)
    prova = models.FileField(upload_to='uploads/')
    

    def __str__(self) -> str:
        return f'Mensagem de {self.profile} + Título {self.title}' 