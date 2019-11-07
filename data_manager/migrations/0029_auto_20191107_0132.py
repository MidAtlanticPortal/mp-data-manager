# Generated by Django 2.2.3 on 2019-11-07 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0028_auto_20191106_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='opacity',
            field=models.FloatField(blank=True, default=0.5, null=True, verbose_name='Initial Opacity'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_color',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_outline_color',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Vector Stroke Color'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_outline_opacity',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Vector Stroke Width'),
        ),
    ]
