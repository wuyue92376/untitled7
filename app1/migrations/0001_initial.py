# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('proline', models.CharField(max_length=30, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='HostInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('HostIP', models.GenericIPAddressField(db_index=True)),
                ('Hostname', models.CharField(max_length=30, db_index=True)),
                ('version', models.CharField(max_length=30)),
                ('app', models.ForeignKey(to='app1.appInfo')),
            ],
        ),
        migrations.CreateModel(
            name='userGroup',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('groups', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=60)),
                ('passwd', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('user_group', models.ForeignKey(default=1, to='app1.userGroup')),
            ],
        ),
    ]
