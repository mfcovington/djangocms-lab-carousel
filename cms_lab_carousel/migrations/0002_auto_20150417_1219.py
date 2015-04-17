# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_migrate_use_structure'),
        ('cms_lab_carousel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('carousel', models.ForeignKey(to='cms_lab_carousel.Carousel')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='slide',
            name='publish_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 17, 19, 19, 41, 130993, tzinfo=utc), help_text='Choose date/time to publish slide. Slides are displayed in reverse-chronological order, so this can be used to control their order. A future date will be hide a slide until that date.', verbose_name='date/time slide published'),
            preserve_default=True,
        ),
    ]
