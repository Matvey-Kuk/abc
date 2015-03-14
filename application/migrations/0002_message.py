# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('from_admin', models.BooleanField(default=False)),
                ('deviceId', models.CharField(max_length=900, default='')),
                ('mail', models.CharField(max_length=100, default='')),
                ('lead', models.ForeignKey(to='application.Lead')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
