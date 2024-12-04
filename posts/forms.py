from django import forms
from .models import Post

class PostForm(forms.ModelForm):

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

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['profile']

        
    title = forms.CharField(
        label='Título da Denúncia',
        widget=forms.TextInput(attrs={'placeholder': 'Dê um título'})

    )
    message = forms.CharField(
        label='Relate o ocorrido',
        widget=forms.Textarea(attrs={'placeholder': 'No dia...'})

    )
    prova = forms.FileField(
        label='Adicione uma Prova Visual do ocorrido',
        widget=forms.ClearableFileInput(attrs={'placeholder': 'Escolha um arquivo para upload'})

    )
    typeOccurrence = forms.ChoiceField(
        label = 'Selecione o tipo de problema:',
        choices = type_choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    

        