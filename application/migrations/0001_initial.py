# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('deviceId', models.CharField(max_length=900, default='')),
                ('mail', models.CharField(max_length=100, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
