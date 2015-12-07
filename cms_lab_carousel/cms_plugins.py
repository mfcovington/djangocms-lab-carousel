from django.core.urlresolvers import reverse
from django.utils import timezone

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Carousel, CarouselPlugin, Slide


class CMSCarouselPlugin(CMSPluginBase):
    model = CarouselPlugin
    module = "Lab Plugins"
    name = "Carousel Plugin"
    render_template = "cms_lab_carousel/plugin.html"

    def render(self, context, instance, placeholder):
        published_slides_list = Slide.objects.filter(
            carousel__id=instance.carousel.id,
            publish_datetime__lte=timezone.now(),
            publish_slide=True,
        ).order_by('-publish_datetime')[:instance.carousel.slide_limit]

        context.update({
            'instance': instance,
            'published_slides_list': published_slides_list,
        })

        menu = context['request'].toolbar.get_or_create_menu('carousel-menu', 'Carousel')

        url_change = reverse('admin:cms_lab_carousel_slide_changelist')
        url_addnew = reverse('admin:cms_lab_carousel_slide_add')
        menu.add_sideframe_item('Edit Slides', url=url_change)
        menu.add_modal_item('Add New Slide', url=url_addnew)
        menu.add_break()

        url_change = reverse('admin:cms_lab_carousel_carousel_changelist')
        url_addnew = reverse('admin:cms_lab_carousel_carousel_add')
        menu.add_sideframe_item('Edit Carousels', url=url_change)
        menu.add_modal_item('Add New Carousel', url=url_addnew)

        return context

plugin_pool.register_plugin(CMSCarouselPlugin)
