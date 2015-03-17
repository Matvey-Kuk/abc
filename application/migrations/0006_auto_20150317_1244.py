# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_remove_message_deviceid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='mail',
            field=models.CharField(max_length=100, blank=True, default=''),
            preserve_default=True,
        ),
    ]
