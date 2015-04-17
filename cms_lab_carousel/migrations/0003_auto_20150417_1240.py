# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cms_lab_carousel', '0002_auto_20150417_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='footer_height',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='header_height',
        ),
        migrations.AlterField(
            model_name='carousel',
            name='slide_limit',
            field=models.IntegerField(default=10, verbose_name='slide limit', validators=[django.core.validators.MinValueValidator(1)], help_text='Specify the maximum # of slides to display.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='other_url_color',
            field=models.CharField(default='default', choices=[('default', 'White'), ('primary', 'Blue'), ('info', 'Light Blue'), ('success', 'Green'), ('warning', 'Orange'), ('danger', 'Red')], blank=True, max_length=7, verbose_name='other URL color', help_text="If there is another relevant URL for this slide, choose the color for it's button."),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='publish_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 19, 40, 36, 175156, tzinfo=utc), verbose_name='date/time slide published', help_text='Choose date/time to publish slide. Slides are displayed in reverse-chronological order, so this can be used to control their order. A future date will be hide a slide until that date.'),
            preserve_default=True,
        ),
    ]
