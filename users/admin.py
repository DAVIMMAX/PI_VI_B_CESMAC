from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefone', 'data_nascimento', 'cpf')  # Campos exibidos na lista
    search_fields = ('user__username', 'user__email', 'cpf')        # Campos para busca
    list_filter = ('data_nascimento',)
