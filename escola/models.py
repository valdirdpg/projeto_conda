from django.db import models

class Professor(models.Model):
    nome = models.CharField('Nome Professor', max_length=100, blank=True)
    rg = models.CharField('Identificação', max_length=12, blank=True)
    data_nascimento = models.DateField('Data de Nascimento', null=True,blank=True)
    endereco = models.CharField('Rua/Bairro', max_length=250, blank=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    cidade = models.CharField('Cidade',max_length=60,blank=True)
    telefone = models.CharField('Telefone/Celular', max_length=15, blank=True)
    data_registro = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nome
