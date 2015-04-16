# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import filer.fields.image
import filer.fields.file
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150416_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text="Specify the carousel's title.", verbose_name='carousel title', max_length=64)),
                ('show_title', models.BooleanField(default=True, help_text="Should the carousel's title be visible?", verbose_name='show carousel title')),
                ('show_header', models.BooleanField(default=True, help_text="Should the carousel's header be visible?", verbose_name='show carousel header')),
                ('show_footer', models.BooleanField(default=True, help_text="Should the carousel's footer be visible?", verbose_name='show carousel footer')),
                ('header_height', models.IntegerField(default=100, help_text="Enter the carousel header's height.", verbose_name='header height (px)', validators=[django.core.validators.MinValueValidator(0)])),
                ('footer_height', models.IntegerField(default=100, help_text="Enter the carousel footer's height.", verbose_name='footer height (px)', validators=[django.core.validators.MinValueValidator(0)])),
                ('slider_height', models.IntegerField(default=390, help_text="Enter the carousel slider's height.", verbose_name='slider height (px)', validators=[django.core.validators.MinValueValidator(100)])),
                ('slider_duration', models.IntegerField(default=8000, help_text='Specify the duration each slide is displayed.', verbose_name='slider duration (milliseconds)', validators=[django.core.validators.MinValueValidator(1000)])),
                ('slide_limit', models.IntegerField(default=0, help_text="Specify the maximum # of slides to display (enter '0' for unlimited).", verbose_name='slide limit', validators=[django.core.validators.MinValueValidator(0)])),
                ('footer_image', filer.fields.image.FilerImageField(blank=True, null=True, help_text='Choose/upload an image for the carousel footer.', related_name='carousel_footer_image', to='filer.Image')),
                ('header_image', filer.fields.image.FilerImageField(blank=True, null=True, help_text='Choose/upload an image for the carousel header.', related_name='carousel_header_image', to='filer.Image')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Enter a title for this slide (e.g., publication title). This will be overlayed on top of this slide.', verbose_name='slide title', max_length=255)),
                ('subtitle', models.CharField(blank=True, help_text='Enter a subtitle for this slide (e.g., publication authors, journal, year). This will be overlayed on top of this slide.', verbose_name='slide subtitle', max_length=255)),
                ('description', models.TextField(blank=True, help_text='Enter a description of this slide (e.g., publication abstract).', verbose_name='slide description')),
                ('image_is_downloadable', models.BooleanField(default=False, help_text='Should the image be downloadable? If so, a download image button will be added to the silde.', verbose_name='image is downloadable')),
                ('pubmed_url', models.URLField(blank=True, help_text='If this slide is for a publication, enter the corresponding PubMed URL.', verbose_name='PubMed URL')),
                ('article_url', models.URLField(blank=True, help_text="If this slide is for a publication, enter the article's URL.", verbose_name='article URL')),
                ('journal_name', models.CharField(blank=True, help_text="If this slide is for a publication, enter the journal's name. It will be displayed on the button linking to the article's URL.", verbose_name='journal name', max_length=20)),
                ('other_url', models.URLField(blank=True, help_text='If there is another relevant URL for this slide, enter it.', verbose_name='other URL')),
                ('other_url_label', models.CharField(blank=True, help_text="If there is another relevant URL for this slide, enter the label for it's button.", verbose_name='other URL label', max_length=20)),
                ('other_url_color', models.CharField(blank=True, help_text="If there is another relevant URL for this slide, choose the color for it's button.", verbose_name='other URL color', max_length=7, choices=[('default', 'White'), ('primary', 'Blue'), ('info', 'Light Blue'), ('success', 'Green'), ('warning', 'Orange'), ('danger', 'Red')])),
                ('publish_slide', models.BooleanField(default=True, help_text='Should this slide be published to the carousel?', verbose_name='publish slide')),
                ('publish_datetime', models.DateTimeField(default=datetime.datetime(2015, 4, 16, 23, 30, 41, 912022, tzinfo=utc), help_text='Choose date/time to publish slide. Slides are displayed in reverse-chronological order, so this can be used to control their order. A future date will be hide a slide until that date.', verbose_name='date/time slide published')),
                ('carousel', models.ForeignKey(to='cms_lab_carousel.Carousel', help_text='Choose a carousel for this slide.')),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', help_text='Choose/upload an image for this slide.', related_name='slide_image')),
                ('pdf', filer.fields.file.FilerFileField(blank=True, null=True, help_text='If this slide is for a publication, choose/upload a PDF for this slide.', related_name='slide_pdf', to='filer.File')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
