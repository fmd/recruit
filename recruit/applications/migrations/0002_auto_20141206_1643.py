# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='key',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='password',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='username',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='candidate',
            field=models.CharField(default=b'', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='application',
            name='test_image',
            field=models.ForeignKey(related_name='tests', blank=True, to='tests.TestImage'),
            preserve_default=True,
        ),
    ]
