# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_migrate_use_structure'),
        ('cms_lab_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='page_link',
            field=cms.models.fields.PageField(help_text='If there is a relevant CMS page for this slide, select it.', on_delete=django.db.models.deletion.SET_NULL, verbose_name='CMS page', related_name='page_link', null=True, to='cms.Page', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slide',
            name='page_link_anchor',
            field=models.CharField(help_text='If relevant, specify an anchor on the linked page.', verbose_name='anchor', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slide',
            name='page_link_color',
            field=models.CharField(help_text="If there is a page link for this slide, choose the color for it's button.", choices=[('default', 'White'), ('primary', 'Blue'), ('info', 'Light Blue'), ('success', 'Green'), ('warning', 'Orange'), ('danger', 'Red')], verbose_name='page link color', max_length=7, default='default', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slide',
            name='page_link_label',
            field=models.CharField(help_text='The default label is the page name. To override the default, enter a new label.', verbose_name='page link label', max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='slide',
            name='page_link_target',
            field=models.BooleanField(help_text='Open page link in a new tab?', default=False, verbose_name='new tab?'),
            preserve_default=True,
        ),
    ]
