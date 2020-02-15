from django.forms import ModelForm, TextInput
from .models import Cidade

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome']
        widgets = {
            'nome': TextInput(attrs={'class': 'input', 'placeholder': 'Nome da Cidade'}),
        }