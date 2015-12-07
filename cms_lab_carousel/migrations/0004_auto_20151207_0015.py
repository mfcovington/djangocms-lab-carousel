# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms_lab_carousel', '0003_auto_20150827_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='carousel',
            field=models.ForeignKey(to='cms_lab_carousel.Carousel', help_text='Choose a carousel for this slide.', on_delete=django.db.models.deletion.SET_NULL, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='publication',
            field=models.ForeignKey(to='cms_lab_publications.Publication', help_text='<strong>If this slide is for a publication, select/create a publication.</strong><br>The publication info will be used to auto-populate the title, subtitle, and description fields when slide is saved (if those fields are left blank).<br>To override this auto-fill behavior, manually enter the title, subtitle, and/or description below.', on_delete=django.db.models.deletion.PROTECT, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='publish_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='<strong>Choose date/time to publish slide.</strong><br>Slides are displayed in reverse-chronological order, so this can be used to control their order. A future date will be hide a slide until that date.<br>If this is a slide for a publication and this field is not set to a future date/time or at least one day in the past, it will be auto-populated with the date of the publication.', verbose_name='date/time slide published'),
            preserve_default=True,
        ),
    ]
