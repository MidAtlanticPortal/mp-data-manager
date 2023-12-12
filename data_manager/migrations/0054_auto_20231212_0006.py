# Generated by Django 3.2.23 on 2023-12-12 00:06

import colorfield.fields
import data_manager.models
import django.contrib.sites.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_manager', '0053_auto_20230703_2345'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='layer',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager('site')),
                ('all_objects', data_manager.models.AllObjectsManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='theme',
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager('site')),
                ('all_objects', data_manager.models.AllObjectsManager()),
            ],
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=25, null=True, samples=[('#FFFFFF', 'white'), ('#888888', 'gray'), ('#000000', 'black'), ('#FF0000', 'red'), ('#FFFF00', 'yellow'), ('#00FF00', 'green'), ('#00FFFF', 'cyan'), ('#0000FF', 'blue'), ('#FF00FF', 'magenta')], verbose_name='Vector Fill Color'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='vector_outline_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=25, null=True, samples=[('#FFFFFF', 'white'), ('#888888', 'gray'), ('#000000', 'black'), ('#FF0000', 'red'), ('#FFFF00', 'yellow'), ('#00FF00', 'green'), ('#00FFFF', 'cyan'), ('#0000FF', 'blue'), ('#FF00FF', 'magenta')], verbose_name='Vector Stroke Color'),
        ),
        migrations.AlterField(
            model_name='lookupinfo',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=25, null=True, samples=[('#FFFFFF', 'white'), ('#888888', 'gray'), ('#000000', 'black'), ('#FF0000', 'red'), ('#FFFF00', 'yellow'), ('#00FF00', 'green'), ('#00FFFF', 'cyan'), ('#0000FF', 'blue'), ('#FF00FF', 'magenta')], verbose_name='Fill Color'),
        ),
        migrations.AlterField(
            model_name='lookupinfo',
            name='stroke_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=25, null=True, samples=[('#FFFFFF', 'white'), ('#888888', 'gray'), ('#000000', 'black'), ('#FF0000', 'red'), ('#FFFF00', 'yellow'), ('#00FF00', 'green'), ('#00FFFF', 'cyan'), ('#0000FF', 'blue'), ('#FF00FF', 'magenta')], verbose_name='Stroke Color'),
        ),
    ]
