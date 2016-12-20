# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import data_manager.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('field_name', models.CharField(max_length=255, null=True, blank=True)),
                ('precision', models.IntegerField(null=True, blank=True)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataNeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('archived', models.BooleanField(default=False)),
                ('description', models.TextField(null=True, blank=True)),
                ('source', models.CharField(max_length=255, null=True, blank=True)),
                ('status', models.TextField(null=True, blank=True)),
                ('contact', models.CharField(max_length=255, null=True, blank=True)),
                ('contact_email', models.CharField(max_length=255, null=True, blank=True)),
                ('expected_date', models.CharField(max_length=255, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveSmallIntegerField(default=10, help_text=b'input an integer to determine the priority/order of the layer being displayed (1 being the highest)', null=True, blank=True)),
                ('slug_name', models.CharField(max_length=100, null=True, blank=True)),
                ('layer_type', models.CharField(help_text=b'use placeholder to temporarily remove layer from TOC', max_length=50, choices=[(b'XYZ', b'XYZ'), (b'WMS', b'WMS'), (b'ArcRest', b'ArcRest'), (b'radio', b'radio'), (b'checkbox', b'checkbox'), (b'Vector', b'Vector'), (b'placeholder', b'placeholder')])),
                ('url', models.CharField(max_length=255, null=True, blank=True)),
                ('shareable_url', models.BooleanField(default=True, help_text=b'Indicates whether the data layer (e.g. map tiles) can be shared with others (through the Map Tiles Link)')),
                ('arcgis_layers', models.CharField(help_text=b'comma separated list of arcgis layer IDs', max_length=255, null=True, blank=True)),
                ('disable_arcgis_attributes', models.BooleanField(default=False, help_text=b'Click to disable clickable ArcRest layers')),
                ('wms_slug', models.CharField(max_length=255, null=True, blank=True)),
                ('wms_version', models.CharField(help_text=b'WMS Versioning - usually either 1.1.1 or 1.3.0', max_length=10, null=True, blank=True)),
                ('is_sublayer', models.BooleanField(default=False)),
                ('search_query', models.BooleanField(default=False, help_text=b'Select when layers are queryable - e.g. MDAT and CAS')),
                ('has_companion', models.BooleanField(default=False, help_text=b'Check if this layer has a companion layer')),
                ('is_disabled', models.BooleanField(default=False, help_text=b'when disabled, the layer will still appear in the TOC, only disabled')),
                ('disabled_message', models.CharField(max_length=255, null=True, blank=True)),
                ('legend', models.CharField(help_text=b'URL or path to the legend image file', max_length=255, null=True, blank=True)),
                ('legend_title', models.CharField(help_text=b'alternative to using the layer name', max_length=255, null=True, blank=True)),
                ('legend_subtitle', models.CharField(max_length=255, null=True, blank=True)),
                ('utfurl', models.CharField(max_length=255, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('data_overview', models.TextField(null=True, blank=True)),
                ('data_source', models.CharField(max_length=255, null=True, blank=True)),
                ('data_notes', models.TextField(null=True, blank=True)),
                ('bookmark', models.CharField(help_text=b'link to view data layer in the planner', max_length=755, null=True, blank=True)),
                ('kml', models.CharField(help_text=b'link to download the KML', max_length=255, null=True, blank=True)),
                ('data_download', models.CharField(help_text=b'link to download the data', max_length=255, null=True, blank=True)),
                ('learn_more', models.CharField(help_text=b'link to view description in the Learn section', max_length=255, null=True, blank=True)),
                ('metadata', models.CharField(help_text=b'link to view/download the metadata', max_length=255, null=True, blank=True)),
                ('source', models.CharField(help_text=b'link back to the data source', max_length=255, null=True, blank=True)),
                ('map_tiles', models.CharField(help_text=b'internal link to a page that details how others might consume the data', max_length=255, null=True, blank=True)),
                ('thumbnail', models.URLField(help_text=b'not sure we are using this any longer...', max_length=255, null=True, blank=True)),
                ('compress_display', models.BooleanField(default=False)),
                ('attribute_event', models.CharField(default=b'click', max_length=35, choices=[(b'click', b'click'), (b'mouseover', b'mouseover')])),
                ('mouseover_field', models.CharField(help_text=b'feature level attribute used in mouseover display', max_length=75, null=True, blank=True)),
                ('lookup_field', models.CharField(max_length=255, null=True, blank=True)),
                ('is_annotated', models.BooleanField(default=False)),
                ('vector_outline_color', models.CharField(max_length=7, null=True, blank=True)),
                ('vector_outline_opacity', models.FloatField(null=True, blank=True)),
                ('vector_color', models.CharField(max_length=7, null=True, blank=True)),
                ('vector_fill', models.FloatField(null=True, blank=True)),
                ('vector_graphic', models.CharField(max_length=255, null=True, blank=True)),
                ('point_radius', models.IntegerField(help_text=b'Used only for for Point layers (default is 2)', null=True, blank=True)),
                ('opacity', models.FloatField(default=0.5, null=True, blank=True)),
                ('attribute_fields', models.ManyToManyField(to='data_manager.AttributeInfo', null=True, blank=True)),
                ('connect_companion_layers_to', models.ManyToManyField(help_text=b'Select which main layer(s) you would like to use in conjuction with this companion layer.', related_name='connect_companion_layers_to_rel_+', null=True, to='data_manager.Layer', blank=True)),
            ],
            options={
            },
            bases=(models.Model, data_manager.models.SiteFlags),
        ),
        migrations.CreateModel(
            name='LookupInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, null=True, blank=True)),
                ('color', models.CharField(max_length=7, null=True, blank=True)),
                ('dashstyle', models.CharField(default=b'solid', max_length=11, choices=[(b'dot', b'dot'), (b'dash', b'dash'), (b'dashdot', b'dashdot'), (b'longdash', b'longdash'), (b'longdashdot', b'longdashdot'), (b'solid', b'solid')])),
                ('fill', models.BooleanField(default=False)),
                ('graphic', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('order', models.PositiveSmallIntegerField(default=10, help_text=b'input an integer to determine the priority/order of the layer being displayed (1 being the highest)', null=True, blank=True)),
                ('visible', models.BooleanField(default=True)),
                ('header_image', models.CharField(max_length=255, null=True, blank=True)),
                ('header_attrib', models.CharField(max_length=255, null=True, blank=True)),
                ('overview', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('thumbnail', models.URLField(max_length=255, null=True, blank=True)),
                ('factsheet_thumb', models.CharField(max_length=255, null=True, blank=True)),
                ('factsheet_link', models.CharField(max_length=255, null=True, blank=True)),
                ('feature_image', models.CharField(max_length=255, null=True, blank=True)),
                ('feature_excerpt', models.TextField(null=True, blank=True)),
                ('feature_link', models.CharField(max_length=255, null=True, blank=True)),
                ('site', models.ManyToManyField(to='sites.Site')),
            ],
            options={
            },
            bases=(models.Model, data_manager.models.SiteFlags),
        ),
        migrations.AddField(
            model_name='layer',
            name='lookup_table',
            field=models.ManyToManyField(to='data_manager.LookupInfo', null=True, blank=True),
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
            name='sublayers',
            field=models.ManyToManyField(related_name='sublayers_rel_+', null=True, to='data_manager.Layer', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='layer',
            name='themes',
            field=models.ManyToManyField(to='data_manager.Theme', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dataneed',
            name='themes',
            field=models.ManyToManyField(to='data_manager.Theme', null=True, blank=True),
            preserve_default=True,
        ),
    ]
