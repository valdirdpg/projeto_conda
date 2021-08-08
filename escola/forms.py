from django import forms
from .models import Professor

class ProfessorForm(forms.Form):
    
    nome = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Digite o seu nome'}))
    ##model = Professor
    fields = ['nome']