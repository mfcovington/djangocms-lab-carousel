from django.contrib import admin
from cms_lab_carousel.models import Carousel, Slide

class CarouselAdmin(admin.ModelAdmin):
    fieldset_frame = ('Carousel Frame', {
        'fields': [
            'title',
            'header_image',
            'footer_image',
        ],
    })

    fieldset_visibility = ('Visibility', {
        'fields': [
            'show_title',
            'show_header',
            'show_footer',
        ],
        'classes': ['collapse'],
    })

    fieldset_dimensions = ('Dimensions', {
        'fields': [
            'header_height',
            'footer_height',
            'slider_height',
        ],
        'classes': ['collapse'],
    })

    fieldset_slides = ('Slide Settings', {
        'fields': [
            'slider_duration',
            'slide_limit',
        ],
        'classes': ['collapse'],
    })

    fieldsets = [
        fieldset_frame,
        fieldset_visibility,
        fieldset_dimensions,
        fieldset_slides,
    ]

    search_fields = ['title']

admin.site.register(Carousel, CarouselAdmin)


class SlideAdmin(admin.ModelAdmin):

    fieldset_basic = ('Basic Slide Info', {
        'fields': [
            'carousel',
            'title',
            'subtitle',
            'description',
            'image',
            'image_is_downloadable',
        ],
    })

    fieldset_article = ('Scientific Article Info', {
        'fields': [
            'pdf',
            'pubmed_url',
            'article_url',
            'journal_name',
        ],
    })

    fieldset_other_url = ('Other URL', {
        'fields': [
            'other_url',
            'other_url_label',
            'other_url_color',
        ],
        'classes': ['collapse'],
    })

    fieldset_publish = ('Publish Settings', {
        'fields': [
            'publish_slide',
            'publish_datetime',
        ],
    })

    fieldsets = [
        fieldset_basic,
        fieldset_article,
        fieldset_other_url,
        fieldset_publish,
    ]

    list_display = ['title', 'carousel', 'publish_slide', 'publish_datetime' ]
    list_filter = ['publish_slide', 'journal_name']
    search_fields = ['title', 'subtitle', 'description']

admin.site.register(Slide, SlideAdmin)

admin.site.site_header = 'CMS Lab Carousel Administration'
