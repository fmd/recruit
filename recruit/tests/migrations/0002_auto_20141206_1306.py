# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimage',
            name='image',
            field=models.CharField(default=b'ubuntu', max_length=100),
            preserve_default=True,
        ),
    ]
