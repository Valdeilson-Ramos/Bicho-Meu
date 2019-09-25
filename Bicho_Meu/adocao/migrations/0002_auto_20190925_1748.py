# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=15, default=None),
        ),
        migrations.AddField(
            model_name='doador',
            name='cpf',
            field=models.CharField(max_length=15, default=None),
        ),
        migrations.AlterField(
            model_name='adocao',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 20, 48, 26, 869273, tzinfo=utc)),
        ),
    ]
