# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20150317_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='mail',
        ),
    ]
