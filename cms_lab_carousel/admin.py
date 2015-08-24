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

    search_fields = ['title']

admin.site.register(Carousel, CarouselAdmin)


class CarouselFilter(admin.SimpleListFilter):
    title = 'Carousel'
    parameter_name = 'carousel'

    def lookups(self, request, model_admin):
        carousel_list = set([slide.carousel for slide in model_admin.model.objects.all()])
        return [(carousel.id, carousel.title) for carousel in carousel_list]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(carousel__id__exact=self.value())
        else:
            return queryset


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
            'publication',
            'pdf',
            'pubmed_url',
            'article_url',
            'journal_name',
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
        fieldset_article,
        fieldset_page_link,
        fieldset_other_url,
        fieldset_publish,
    ]

    list_display = ['title', 'carousel', 'publish_slide', 'publish_datetime' ]
    list_filter = [CarouselFilter, 'publish_slide', 'journal_name']
    search_fields = ['title', 'subtitle', 'description']

admin.site.register(Slide, SlideAdmin)

admin.site.site_header = 'CMS Lab Carousel Administration'
