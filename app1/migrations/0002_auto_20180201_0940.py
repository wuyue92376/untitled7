# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='app',
            field=models.ForeignKey(null=True, to='app1.appInfo'),
        ),
    ]
