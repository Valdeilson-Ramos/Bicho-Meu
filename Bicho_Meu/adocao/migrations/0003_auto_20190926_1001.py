# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('adocao', '0002_auto_20190926_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adocao',
            name='registro',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 26, 13, 1, 52, 550058, tzinfo=utc)),
        ),
    ]
