# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('container', models.CharField(default=b'', max_length=100)),
                ('candidate', models.CharField(max_length=255)),
                ('test_image', models.ForeignKey(related_name='tests', to='tests.TestImage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
