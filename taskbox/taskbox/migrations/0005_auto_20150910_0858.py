# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskbox', '0004_auto_20150909_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'open', max_length=255, choices=[(b'open', b'Open'), (b'in_progress', b'In Progress'), (b'done', b'Done')]),
        ),
    ]
