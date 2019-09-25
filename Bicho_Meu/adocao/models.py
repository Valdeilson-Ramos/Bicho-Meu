from django.db import models
from django.utils import timezone


class Raca(models.Model):
    PORTES = (('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'))
    nome = models.CharField(max_length=200)
    porte = models.CharField(max_length=2,choices=PORTES)


class Doador(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15,default=None)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2,choices=GENEROS)



class Animal(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    especie = models.CharField(max_length=30)
    descricao = models.TextField()
    registro = models.DateTimeField(auto_now_add=True)
    raca = models.ForeignKey('Raca')
    doador = models.ForeignKey('Doador')


class Cliente(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15,default=None)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2,choices=GENEROS)


class Adocao(models.Model):
    registro = models.DateTimeField(default=timezone.now())
    animal = models.ForeignKey('Animal')
    cliente = models.ForeignKey('Cliente')
