from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms_lab_carousel.models import CarouselPlugin

from django.utils import timezone

from cms_lab_carousel.models import Carousel, Slide

class CMSCarouselPlugin(CMSPluginBase):
    model = CarouselPlugin
    module = "Carousels"
    name = "Carousel Plugin"
    render_template = "cms_lab_carousel/plugin.html"

    def render(self, context, instance, placeholder):
        # context.update({'instance': instance,})

        # Slide.objects.filter(carousel__id=instance.id)
        # context['current_list'] = Scientist.objects.filter(current=True)

        published_slides_list = Slide.objects.filter(
            carousel__id=instance.carousel.id,
            publish_datetime__lte=timezone.now(),
            publish_slide=True,
        ).order_by('-publish_datetime')[:instance.carousel.slide_limit]

        context.update({
            'instance': instance,
            'published_slides_list': published_slides_list,
        })
        return context

plugin_pool.register_plugin(CMSCarouselPlugin)


