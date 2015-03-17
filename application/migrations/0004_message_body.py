# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_message_hasbeenread'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.CharField(max_length=2000, default=''),
            preserve_default=True,
        ),
    ]
