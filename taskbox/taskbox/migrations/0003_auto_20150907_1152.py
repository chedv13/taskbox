# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskbox', '0002_auto_20150902_0800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
