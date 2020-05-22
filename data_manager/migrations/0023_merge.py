# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0022_auto_20180501_2245'),
        ('data_manager', '0020_auto_20180808_2254'),
    ]

    operations = [
        # From migration 0025 on the MidAtlantic Fork and from 0033 on the Ecotrust Fork
        #   This file is the lowest common denominator.
        migrations.AddField(
            model_name='layer',
            name='show_legend',
            field=models.BooleanField(default=True, help_text='show the legend for this layer if available'),
        ),
    ]
