from django.contrib import admin
from cms_lab_carousel.models import Carousel

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

admin.site.site_header = 'CMS Lab Carousel Administration'
