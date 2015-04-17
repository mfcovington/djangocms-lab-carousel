# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import filer.fields.file
import filer.fields.image
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_migrate_use_structure'),
        ('filer', '0003_auto_20150417_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=64, help_text="Specify the carousel's title.", verbose_name='carousel title')),
                ('show_title', models.BooleanField(verbose_name='show carousel title', help_text="Should the carousel's title be visible?", default=True)),
                ('show_header', models.BooleanField(verbose_name='show carousel header', help_text="Should the carousel's header be visible?", default=True)),
                ('show_footer', models.BooleanField(verbose_name='show carousel footer', help_text="Should the carousel's footer be visible?", default=True)),
                ('slider_height', models.IntegerField(verbose_name='slider height (px)', validators=[django.core.validators.MinValueValidator(100)], help_text="Enter the carousel slider's height.", default=390)),
                ('slider_duration', models.IntegerField(verbose_name='slider duration (milliseconds)', validators=[django.core.validators.MinValueValidator(1000)], help_text='Specify the duration each slide is displayed.', default=8000)),
                ('slide_limit', models.IntegerField(verbose_name='slide limit', validators=[django.core.validators.MinValueValidator(1)], help_text='Specify the maximum # of slides to display.', default=10)),
                ('footer_image', filer.fields.image.FilerImageField(related_name='carousel_footer_image', null=True, help_text='Choose/upload an image for the carousel footer.', blank=True, to='filer.Image')),
                ('header_image', filer.fields.image.FilerImageField(related_name='carousel_header_image', null=True, help_text='Choose/upload an image for the carousel header.', blank=True, to='filer.Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarouselPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='cms.CMSPlugin')),
                ('carousel', models.ForeignKey(to='cms_lab_carousel.Carousel')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255, help_text='Enter a title for this slide (e.g., publication title). This will be overlayed on top of this slide.', verbose_name='slide title')),
                ('subtitle', models.CharField(max_length=255, help_text='Enter a subtitle for this slide (e.g., publication authors, journal, year). This will be overlayed on top of this slide.', verbose_name='slide subtitle', blank=True)),
                ('description', models.TextField(help_text='Enter a description of this slide (e.g., publication abstract).', verbose_name='slide description', blank=True)),
                ('image_is_downloadable', models.BooleanField(verbose_name='image is downloadable', help_text='Should the image be downloadable? If so, a download image button will be added to the silde.', default=False)),
                ('pubmed_url', models.URLField(help_text='If this slide is for a publication, enter the corresponding PubMed URL.', verbose_name='PubMed URL', blank=True)),
                ('article_url', models.URLField(help_text="If this slide is for a publication, enter the article's URL.", verbose_name='article URL', blank=True)),
                ('journal_name', models.CharField(max_length=20, help_text="If this slide is for a publication, enter the journal's name. It will be displayed on the button linking to the article's URL.", verbose_name='journal name', blank=True)),
                ('other_url', models.URLField(help_text='If there is another relevant URL for this slide, enter it.', verbose_name='other URL', blank=True)),
                ('other_url_label', models.CharField(max_length=20, help_text="If there is another relevant URL for this slide, enter the label for it's button.", verbose_name='other URL label', blank=True)),
                ('other_url_color', models.CharField(help_text="If there is another relevant URL for this slide, choose the color for it's button.", default='default', verbose_name='other URL color', choices=[('default', 'White'), ('primary', 'Blue'), ('info', 'Light Blue'), ('success', 'Green'), ('warning', 'Orange'), ('danger', 'Red')], max_length=7, blank=True)),
                ('publish_slide', models.BooleanField(verbose_name='publish slide', help_text='Should this slide be published to the carousel?', default=True)),
                ('publish_datetime', models.DateTimeField(verbose_name='date/time slide published', help_text='Choose date/time to publish slide. Slides are displayed in reverse-chronological order, so this can be used to control their order. A future date will be hide a slide until that date.', default=django.utils.timezone.now)),
                ('carousel', models.ForeignKey(help_text='Choose a carousel for this slide.', to='cms_lab_carousel.Carousel')),
                ('image', filer.fields.image.FilerImageField(related_name='slide_image', help_text='Choose/upload an image for this slide.', to='filer.Image')),
                ('pdf', filer.fields.file.FilerFileField(related_name='slide_pdf', null=True, help_text='If this slide is for a publication, choose/upload a PDF for this slide.', blank=True, to='filer.File')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
