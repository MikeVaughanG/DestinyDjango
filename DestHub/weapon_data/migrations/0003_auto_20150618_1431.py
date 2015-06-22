# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapon_data', '0002_weapon'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='weapon_damage_types',
            field=models.CharField(default='NA', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weapon',
            name='weapon_rolls',
            field=models.CharField(default='NA', max_length=600),
            preserve_default=False,
        ),
    ]
