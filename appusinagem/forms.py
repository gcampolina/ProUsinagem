from django import forms
from .models import Service, Clientes



class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['contratante', 'nome_servico', 'detalhes', 'data_servico', 'data_entrega', 'contato', 'total', 'imagem']
        widgets = {
            'data_servico': forms.DateInput(attrs={'type': 'date'}),
            'data_entrega': forms.DateInput(attrs={'type': 'date'}),
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'email', 'telefone', 'endereco']