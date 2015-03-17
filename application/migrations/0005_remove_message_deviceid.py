# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_message_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='deviceId',
        ),
    ]
