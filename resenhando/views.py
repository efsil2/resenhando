from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Filme

def lista_filmes(request):
       film= Filme.objects.filter(Publicado__lte=timezone.now()).order_by('Publicado')
       return render(request,'resenhando/lista_filmes.html',{'film':film})