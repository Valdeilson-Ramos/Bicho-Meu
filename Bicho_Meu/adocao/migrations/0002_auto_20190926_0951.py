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
        migrations.AlterField(
            model_name='adocao',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 26, 12, 51, 39, 206001, tzinfo=utc)),
        ),
    ]
