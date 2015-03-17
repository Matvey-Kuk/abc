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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('deviceId', models.CharField(max_length=900, default='')),
                ('mail', models.CharField(blank=True, max_length=100, default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('has_been_read_by_sender', models.BooleanField(default=False)),
                ('has_been_read_by_receiver', models.BooleanField(default=False)),
                ('body', models.CharField(max_length=10000, default='')),
                ('from_lead', models.ForeignKey(to='application.Lead', related_name='message_from_lead')),
                ('to_lead', models.ForeignKey(to='application.Lead', related_name='message_to_lead')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
