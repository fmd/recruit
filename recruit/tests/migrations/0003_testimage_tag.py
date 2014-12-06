# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20141206_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimage',
            name='tag',
            field=models.CharField(default=b'recruit', max_length=100),
            preserve_default=True,
        ),
    ]
