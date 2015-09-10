# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskbox', '0003_auto_20150907_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=255, choices=[(b'open', b'Open'), (b'in_progress', b'In Progress'), (b'done', b'Done')]),
        ),
    ]
