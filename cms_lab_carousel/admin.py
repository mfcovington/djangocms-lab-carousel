from django.contrib import admin

from .models import Carousel, Slide


@admin.register(Carousel)
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

    fieldset_slides = ('Slide Settings', {
        'fields': [
            'slider_height',
            'slider_duration',
            'slide_limit',
        ],
        'classes': ['collapse'],
    })

    fieldsets = [
        fieldset_frame,
        fieldset_visibility,
        fieldset_slides,
    ]

    save_on_top = True
    search_fields = ['title']


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):

    fieldset_basic = ('Basic Slide Info', {
        'fields': [
            'carousel',
            'publication',
            'title',
            'subtitle',
            'description',
            'image',
            'image_is_downloadable',
        ],
    })

    fieldset_page_link = ('Page Link', {
        'fields': [
            'page_link',
            'page_link_label',
            'page_link_color',
            'page_link_anchor',
            'page_link_target',
        ],
        'classes': ['collapse'],
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
        fieldset_page_link,
        fieldset_other_url,
        fieldset_publish,
    ]

    list_display = ['title', 'carousel', 'publish_slide', 'publish_datetime' ]
    list_filter = ['publish_slide', 'carousel']
    save_on_top = True
    search_fields = ['title', 'subtitle', 'description']


admin.site.site_header = 'CMS Lab Carousel Administration'
