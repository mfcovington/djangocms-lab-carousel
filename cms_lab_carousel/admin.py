from django.contrib import admin
from django.db.models import Count

from .models import Carousel, Slide


class SlideCounter():
    """
    Display (and sort by) number of slides associated with a carousel.
    """

    def get_queryset(self, request):
        queryset = self.model.objects.get_queryset()
        return queryset.annotate(slide_counter=Count('slide', distinct=True))

    def slide_counter(self, obj):
        return obj.slide_counter

    slide_counter.admin_order_field = 'slide_counter'
    slide_counter.short_description = '# of Slides'


@admin.register(Carousel)
class CarouselAdmin(SlideCounter, admin.ModelAdmin):
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

    list_display = [
        'title',
        'slide_counter',
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
