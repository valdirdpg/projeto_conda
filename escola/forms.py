from django import forms
from .models import Professor

class ProfessorForm(forms.Form):
    
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite o seu nome'}))
    rg =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Somente números'}))
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Data de Nascimento'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Rua/Bairro'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'CEP'}))
    cidade = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Cidade'}))
    telefone = forms.CharField(widget=forms.NumberInput(attrs={'placeholder':'Telefone/Celular'}))
    #data_registro = models.CharField('Data de registro')
    ##model = Professor
    fields = ['__all__']