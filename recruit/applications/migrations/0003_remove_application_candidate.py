# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_auto_20141206_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='candidate',
        ),
    ]
