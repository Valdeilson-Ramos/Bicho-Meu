from django.db import models
from django.utils import timezone


class Raca(models.Model):
    PORTES = (('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande'))
    nome = models.CharField(max_length=200)
    porte = models.CharField(max_length=2,choices=PORTES)

    def __str__(self):
        return 'Raça - {}'.format(self.nome)

    class Meta:
        verbose_name_plural = 'Raças'

class Doador(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15,default=None, verbose_name="CPF")
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2,choices=GENEROS)

    def __str__(self):
        return 'Doador - {}'.format(self.nome)

    def registro_eh_antigo(self):
        um_ano = timezone.now() - datetime.timedelta(days=365)
        return self.registro < um_ano
    registro_eh_antigo.admin_order_field = 'registro'
    registro_eh_antigo.boolean = True
    registro_eh_antigo.short_description = 'Doador antigo?'

    class Meta:
        verbose_name_plural = 'Doadores'

class Animal(models.Model):
    nome = models.CharField(max_length=200)
    idade = models.IntegerField(default=0)
    especie = models.CharField(max_length=30)
    descricao = models.TextField()
    registro = models.DateTimeField(auto_now_add=True)
    raca = models.ForeignKey('Raca')
    doador = models.ForeignKey('Doador')

    def __str__(self):
        return 'Animal - {}'.format(self.nome)

    class Meta:
        verbose_name_plural = 'Animais'

class Cliente(models.Model):
    GENEROS = (('M', 'Masculino'), ('F', 'Feminino'))
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15,default=None, verbose_name="CPF")
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    registro = models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=2,choices=GENEROS)

    def __str__(self):
        return 'Cliente - {}'.format(self.nome)

    def registro_eh_antigo(self):
        um_ano = timezone.now() - datetime.timedelta(days=365)
        return self.registro < um_ano
    registro_eh_antigo.admin_order_field = 'registro'
    registro_eh_antigo.boolean = True
    registro_eh_antigo.short_description = 'Cliente antigo?'


class Adocao(models.Model):
    registro = models.DateTimeField(default=timezone.now())
    animal = models.ForeignKey('Animal')
    cliente = models.ForeignKey('Cliente')

    def __str__(self):
        return 'Adocao - {} - {}'.format(self.animal, self.cliente)

    class Meta:
        verbose_name_plural = 'Adoções'
