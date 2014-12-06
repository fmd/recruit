# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(default=b'', max_length=100)),
                ('image', models.CharField(default=b'ubuntu:latest', max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
