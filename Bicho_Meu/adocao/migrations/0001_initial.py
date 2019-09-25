# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('registro', models.DateTimeField(default=datetime.datetime(2019, 9, 25, 20, 37, 50, 749911, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('idade', models.IntegerField(default=0)),
                ('especie', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(max_length=2, choices=[('M', 'Masculino'), ('F', 'Feminino')])),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(max_length=2, choices=[('M', 'Masculino'), ('F', 'Feminino')])),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('porte', models.CharField(max_length=2, choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande')])),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='doador',
            field=models.ForeignKey(to='adocao.Doador'),
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.ForeignKey(to='adocao.Raca'),
        ),
        migrations.AddField(
            model_name='adocao',
            name='animal',
            field=models.ForeignKey(to='adocao.Animal'),
        ),
        migrations.AddField(
            model_name='adocao',
            name='cliente',
            field=models.ForeignKey(to='adocao.Cliente'),
        ),
    ]
