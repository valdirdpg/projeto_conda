from django.db import models

class Professor(models.Model):
    nome = models.CharField('Nome Professor', max_length=100)
    
    def __str__(self):
        return self.nome
