# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms_lab_publications', '0001_initial'),
        ('cms_lab_carousel', '0002_auto_20150508_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='article_url',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='journal_name',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='pubmed_url',
        ),
        migrations.AddField(
            model_name='slide',
            name='publication',
            field=models.ForeignKey(help_text='<strong>If this slide is for a publication, select/create a publication.</strong><br>The publication info will be used to auto-populate the title, subtitle, and description fields when slide is saved (if those fields are left blank).<br>To override this auto-fill behavior, manually enter the title, subtitle, and/or description below.', blank=True, to='cms_lab_publications.Publication', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='description',
            field=models.TextField(blank=True, help_text='<strong>Enter a description of this slide.</strong><br>If this is a slide for a publication and this field is left blank, it will be auto-populated with the abstract of the publication.', verbose_name='slide description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='slide_image', help_text='<strong>Choose/upload an image for this slide.</strong><br>If this is a slide for a publication and this field is left blank, the image for the publication will be used.', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='other_url_color',
            field=models.CharField(help_text='If there is another relevant URL for this slide, choose the color for its button.', default='default', blank=True, choices=[('default', 'White'), ('primary', 'Blue'), ('info', 'Light Blue'), ('success', 'Green'), ('warning', 'Orange'), ('danger', 'Red')], max_length=7, verbose_name='other URL color'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='other_url_label',
            field=models.CharField(blank=True, help_text='If there is another relevant URL for this slide, enter the label for its button.', max_length=20, verbose_name='other URL label'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='page_link_color',
            field=models.CharField(help_text='If there is a page link for this slide, choose the color for its button.', default='default', blank=True, choices=[('default', 'White'), ('primary', 'Blue'), ('info', 'Light Blue'), ('success', 'Green'), ('warning', 'Orange'), ('danger', 'Red')], max_length=7, verbose_name='page link color'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='subtitle',
            field=models.CharField(blank=True, help_text='<strong>Enter a subtitle to be overlayed on top of this slide.</strong><br>If this is a slide for a publication and this field is left blank, it will be auto-populated with the citation for the publication.', max_length=255, verbose_name='slide subtitle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='title',
            field=models.CharField(blank=True, help_text='<strong>Enter a title to be overlayed on top of this slide.</strong><br>If this is a slide for a publication and this field is left blank, it will be auto-populated with the title of the publication.', max_length=255, verbose_name='slide title'),
            preserve_default=True,
        ),
    ]
