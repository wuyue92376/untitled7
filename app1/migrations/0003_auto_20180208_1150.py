# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180201_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostinfo',
            name='admin',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='passwd',
            field=models.CharField(null=True, max_length=60),
        ),
    ]
