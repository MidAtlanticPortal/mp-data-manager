# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('data_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='connect_companion_layers_to',
            field=models.ManyToManyField(help_text=b'Select which main layer(s) you would like to use in conjuction with this companion layer.', related_name='connect_companion_layers_to_rel_+', null=True, to='data_manager.Layer', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='disable_arcgis_attributes',
            field=models.BooleanField(default=False, help_text=b'Click to disable clickable ArcRest layers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='has_companion',
            field=models.BooleanField(default=False, help_text=b'Check if this layer has a companion layer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='order',
            field=models.PositiveSmallIntegerField(default=10, help_text=b'input an integer to determine the priority/order of the layer being displayed (1 being the highest)', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='point_radius',
            field=models.IntegerField(help_text=b'Used only for for Point layers (default is 2)', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='search_query',
            field=models.BooleanField(default=False, help_text=b'Select when layers are queryable - e.g. MDAT and CAS'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='wms_slug',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='wms_version',
            field=models.CharField(help_text=b'WMS Versioning - usually either 1.1.1 or 1.3.0', max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='theme',
            name='order',
            field=models.PositiveSmallIntegerField(default=10, help_text=b'input an integer to determine the priority/order of the layer being displayed (1 being the highest)', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='theme',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
            preserve_default=True,
        ),
    ]
