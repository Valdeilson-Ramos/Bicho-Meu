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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('registro', models.DateTimeField(default=datetime.datetime(2019, 9, 26, 12, 27, 12, 596820, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=15, default=None)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=15, default=None)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('porte', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Medio'), ('G', 'Grande')], max_length=2)),
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
