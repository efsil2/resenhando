import site
import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
    

generos = [('Ação', 'Ação'),('Animação','Animação'),('Comedia','Comedia'),('Drama','Drama'),
        ('Ficção científica','Ficção científica'),('Infantil','Infantil'),('Suspense','Suspense'),
        ('Terror','Terror'),('Outros','Outros')]

classificação = [('Livre','Livre'),('+12','+12'),('+10','+10'),('+14','+14'),('+16','+16'),('+18','+18')]


class Filme(models.Model):
    Titulo = models.CharField(max_length=100)
    Estreia = models.DateField()
    Diretores = models.CharField(blank=True, null=True, max_length=100)
    Estrelando = models.CharField(max_length=100,blank=True, null=True)
    Resenha = models.TextField(max_length=250)
    Genero = models.CharField(choices=generos, max_length=20,blank=True, null=True)
    Classificação = models.CharField(choices=classificação, max_length=10,blank=True, null=True)
    Produção = models.CharField(max_length=100,blank=True, null=True)
    Edição = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Publicado = models.DateTimeField('Postado em')

    def publicado_desde(self):
        return self.Publicado(timezone.now())  

    def __str__(self):
        return self.Resenha
        





