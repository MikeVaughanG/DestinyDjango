# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapon_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weapon_name', models.CharField(max_length=300)),
                ('weapon_tier', models.CharField(max_length=35)),
                ('weapon_descrip', models.CharField(max_length=600)),
                ('weapon_type', models.CharField(max_length=35)),
            ],
        ),
    ]
