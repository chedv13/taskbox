# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskbox', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='closed',
            new_name='done',
        ),
    ]
