# Generated by Django 2.2.3 on 2019-07-30 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0026_auto_20190725_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='filterable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='layer',
            name='geoportal_id',
            field=models.CharField(blank=True, default=None, help_text='GeoPortal UUID', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='disabled_message',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='espis_region',
            field=models.CharField(blank=True, choices=[('Mid Atlantic', 'Mid Atlantic')], default=True, help_text='Region to search within', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='espis_search',
            field=models.CharField(blank=True, default=True, help_text='keyphrase search for ESPIS Link', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='learn_more',
            field=models.CharField(blank=True, default=None, help_text='link to view description in the Learn section', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='mouseover_field',
            field=models.CharField(blank=True, default=True, help_text='feature level attribute used in mouseover display', max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='point_radius',
            field=models.IntegerField(blank=True, default=True, help_text='Used only for for Point layers (default is 2)', null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='thumbnail',
            field=models.URLField(blank=True, default=None, help_text='not sure we are using this any longer...', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_color',
            field=models.CharField(blank=True, default=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_fill',
            field=models.FloatField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_graphic',
            field=models.CharField(blank=True, default=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_outline_color',
            field=models.CharField(blank=True, default=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_outline_opacity',
            field=models.FloatField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_additional',
            field=models.TextField(blank=True, default=None, help_text='additional WMS key-value pairs: &key=value...', null=True, verbose_name='WMS Additional Fields'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_format',
            field=models.CharField(blank=True, default=None, help_text='most common: image/png. Only image types supported.', max_length=100, null=True, verbose_name='WMS Format'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_srs',
            field=models.CharField(blank=True, default=None, help_text='If not EPSG:3857 WMS requests will be proxied', max_length=100, null=True, verbose_name='WMS SRS'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_styles',
            field=models.CharField(blank=True, default=None, help_text='pre-determined styles, if exist', max_length=255, null=True, verbose_name='WMS Styles'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_time_item',
            field=models.CharField(blank=True, default=None, help_text='Time Attribute Field, if different from "TIME". Proxy only.', max_length=255, null=True, verbose_name='WMS Time Field'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_timing',
            field=models.CharField(blank=True, default=None, help_text='http://docs.geoserver.org/stable/en/user/services/wms/time.html#specifying-a-time', max_length=255, null=True, verbose_name='WMS Time'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='wms_version',
            field=models.CharField(blank=True, choices=[(None, ''), ('1.0.0', '1.0.0'), ('1.1.0', '1.1.0'), ('1.1.1', '1.1.1'), ('1.3.0', '1.3.0')], default=None, help_text='WMS Versioning - usually either 1.1.1 or 1.3.0', max_length=10, null=True),
        ),
    ]
