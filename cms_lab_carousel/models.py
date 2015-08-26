from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField

from cms_lab_publications.models import Publication


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
        default=10,
        help_text="Specify the maximum # of slides to display.",
        validators=[
            MinValueValidator(1),
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
        blank=True,
        help_text='Enter a title to be overlayed on top of this slide.<br>' \
                  'If this is a slide for a publication and this field is ' \
                  'left blank, it will be auto-populated with the ' \
                  'title of the publication.',
        max_length=255,
    )
    subtitle = models.CharField('slide subtitle',
        blank=True,
        help_text='Enter a subtitle to be overlayed on top of this slide.<br>' \
                  'If this is a slide for a publication and this field is ' \
                  'left blank, it will be auto-populated with the ' \
                  'citation for the publication.',
        max_length=255,
    )
    description = models.TextField('slide description',
        blank=True,
        help_text='Enter a description of this slide.<br>' \
                  'If this is a slide for a publication and this field is ' \
                  'left blank, it will be auto-populated with the ' \
                  'abstract of the publication.',
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

    publication = models.ForeignKey(Publication,
        help_text='<strong>If this slide is for a publication, ' \
                  'select/create a publication.</strong><br>' \
                  'The publication info will be used to auto-populate the ' \
                  'title, subtitle, and description fields when slide ' \
                  'is saved (if those fields are left blank).<br>' \
                  'To override this auto-fill behavior, manually enter ' \
                  'the title, subtitle, and/or description below.',
        blank=True,
        null=True,
    )

    page_link = PageField(
        blank=True,
        null=True,
        help_text="If there is a relevant CMS page for this slide, select it.",
        on_delete=models.SET_NULL,
        related_name='page_link',
        verbose_name="CMS page",
    )
    page_link_label = models.CharField('page link label',
        blank=True,
        help_text="The default label is the page name. " \
                  "To override the default, enter a new label.",
        max_length=20,
    )
    page_link_color = models.CharField('page link color',
        blank=True,
        choices=URL_COLOR_CHOICES,
        default='default',
        help_text="If there is a page link for this slide, " \
                  "choose the color for it's button.",
        max_length=7,
    )
    page_link_anchor = models.CharField("anchor",
        blank=True,
        help_text="If relevant, specify an anchor on the linked page.",
        max_length=255,
    )
    page_link_target = models.BooleanField("new tab?",
        default=False,
        help_text='Open page link in a new tab?',
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
        default='default',
        help_text="If there is another relevant URL for this slide, " \
                  "choose the color for it's button.",
        max_length=7,
    )

    publish_slide = models.BooleanField('publish slide',
        default=True,
        help_text='Should this slide be published to the carousel?',
    )
    publish_datetime = models.DateTimeField('date/time slide published',
        default=timezone.now,
        help_text='Choose date/time to publish slide. ' \
                  'Slides are displayed in reverse-chronological order, ' \
                  'so this can be used to control their order. ' \
                  'A future date will be hide a slide until that date.',
    )

    def save(self, *args, **kwargs):
        """
        Before saving, if slide is for a publication, use publication info
        for slide's title, subtitle, description.
        """
        if self.publication:
            publication = self.publication

            if not self.title:
                self.title = publication.title

            if not self.subtitle:
                first_author = publication.first_author

                if first_author == publication.last_author:
                    authors = first_author
                else:
                    authors = '{} et al.'.format(first_author)

                self.subtitle = '{}, {} ({})'.format(authors,
                    publication.journal, publication.year)

            if not self.description:
                self.description = publication.abstract

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CarouselPlugin (CMSPlugin):
    carousel = models.ForeignKey('cms_lab_carousel.Carousel')

    def __str__(self):
        return self.carousel.title
