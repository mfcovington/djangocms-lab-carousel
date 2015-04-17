from cms.models import CMSPlugin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

class Carousel(models.Model):

    title = models.CharField('carousel title',
        help_text="Specify the carousel's title.",
        max_length=64,
    )
    header_image = FilerImageField(
        blank=True,
        null=True,
        help_text='Choose/upload an image for the carousel header.',
        related_name='carousel_header_image',
    )
    footer_image = FilerImageField(
        blank=True,
        null=True,
        help_text='Choose/upload an image for the carousel footer.',
        related_name='carousel_footer_image',
    )

    show_title = models.BooleanField('show carousel title',
        help_text="Should the carousel's title be visible?",
        default=True,
    )
    show_header = models.BooleanField('show carousel header',
        help_text="Should the carousel's header be visible?",
        default=True,
    )
    show_footer = models.BooleanField('show carousel footer',
        help_text="Should the carousel's footer be visible?",
        default=True,
    )

    header_height = models.IntegerField('header height (px)',
        default=100,
        help_text="Enter the carousel header's height.",
        validators=[
            MinValueValidator(0),
        ]
    )
    footer_height = models.IntegerField('footer height (px)',
        default=100,
        help_text="Enter the carousel footer's height.",
        validators=[
            MinValueValidator(0),
        ]
    )
    slider_height = models.IntegerField('slider height (px)',
        default=390,
        help_text="Enter the carousel slider's height.",
        validators=[
            MinValueValidator(100),
        ]
    )

    slider_duration = models.IntegerField('slider duration (milliseconds)',
        default=8000,
        help_text='Specify the duration each slide is displayed.',
        validators=[
            MinValueValidator(1000),
        ]
    )
    slide_limit = models.IntegerField('slide limit',
        default=0,
        help_text="Specify the maximum # of slides to display (enter '0' for unlimited).",
        validators=[
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return self.title

class Slide(models.Model):

    URL_COLOR_CHOICES = (
        ('default', 'White'),
        ('primary', 'Blue'),
        ('info', 'Light Blue'),
        ('success', 'Green'),
        ('warning', 'Orange'),
        ('danger', 'Red'),
    )

    carousel = models.ForeignKey('cms_lab_carousel.Carousel',
        help_text='Choose a carousel for this slide.',
    )

    title = models.CharField('slide title',
        help_text='Enter a title for this slide (e.g., publication title). ' \
                  'This will be overlayed on top of this slide.',
        max_length=255,
    )
    subtitle = models.CharField('slide subtitle',
        help_text='Enter a subtitle for this slide (e.g., publication authors, journal, year). ' \
                  'This will be overlayed on top of this slide.',
        blank=True,
        max_length=255,
    )
    description = models.TextField('slide description',
        blank=True,
        help_text='Enter a description of this slide (e.g., publication abstract).',
    )
    image = FilerImageField(
        help_text='Choose/upload an image for this slide.',
        related_name='slide_image',
    )
    image_is_downloadable = models.BooleanField('image is downloadable',
        help_text='Should the image be downloadable? ' \
                  'If so, a download image button will be added to the silde.',
        default=False,
    )

    pdf = FilerFileField(
        blank=True,
        null=True,
        help_text='If this slide is for a publication, choose/upload a PDF for this slide.',
        related_name='slide_pdf',
    )
    pubmed_url = models.URLField('PubMed URL',
        blank=True,
        help_text='If this slide is for a publication, enter the corresponding PubMed URL.',
    )
    article_url = models.URLField('article URL',
        blank=True,
        help_text="If this slide is for a publication, enter the article's URL.",
    )
    journal_name = models.CharField('journal name',
        blank=True,
        max_length=20,
        help_text="If this slide is for a publication, enter the journal's name. " \
                  "It will be displayed on the button linking to the article's URL.",
    )
    other_url = models.URLField('other URL',
        blank=True,
        help_text='If there is another relevant URL for this slide, enter it.',
    )
    other_url_label = models.CharField('other URL label',
        blank=True,
        help_text="If there is another relevant URL for this slide, " \
                  "enter the label for it's button.",
        max_length=20,
    )
    other_url_color = models.CharField('other URL color',
        blank=True,
        choices=URL_COLOR_CHOICES,
        help_text="If there is another relevant URL for this slide, " \
                  "choose the color for it's button.",
        max_length=7,
    )

    publish_slide = models.BooleanField('publish slide',
        default=True,
        help_text='Should this slide be published to the carousel?',
    )
    publish_datetime = models.DateTimeField('date/time slide published',
        default=timezone.now(),
        help_text='Choose date/time to publish slide. ' \
                  'Slides are displayed in reverse-chronological order, ' \
                  'so this can be used to control their order. ' \
                  'A future date will be hide a slide until that date.',
    )

    def __str__(self):
        return self.title


class CarouselPlugin (CMSPlugin):
    carousel = models.ForeignKey('cms_lab_carousel.Carousel')

    def __str__(self):
        return self.carousel.title
