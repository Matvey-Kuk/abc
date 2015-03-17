# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='hasBeenRead',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
