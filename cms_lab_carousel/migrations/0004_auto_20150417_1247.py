# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms_lab_carousel', '0003_auto_20150417_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='publish_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date/time slide published', help_text='Choose date/time to publish slide. Slides are displayed in reverse-chronological order, so this can be used to control their order. A future date will be hide a slide until that date.'),
            preserve_default=True,
        ),
    ]
