# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weapon_data', '0004_auto_20150618_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weapon',
            name='weapon_rolls',
            field=models.CharField(max_length=10000),
        ),
    ]
