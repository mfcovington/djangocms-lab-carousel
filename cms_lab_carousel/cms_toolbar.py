from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar.items import Break, SubMenu
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


@toolbar_pool.register
class CarouselToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu(
            ADMIN_MENU_IDENTIFIER, _('Apps')
        )

        position = admin_menu.get_alphabetical_insert_position(
            _('Carousel'),
            SubMenu
        )

        if not position:
            position = admin_menu.find_first(
                Break,
                identifier=ADMINISTRATION_BREAK
            ) + 1
            admin_menu.add_break('custom-break', position=position)

        carousel_menu = admin_menu.get_or_create_menu(
            'carousel-menu',
            _('Carousel ...'),
            position=position
        )

        url_change = reverse('admin:cms_lab_carousel_slide_changelist')
        url_addnew = reverse('admin:cms_lab_carousel_slide_add')
        carousel_menu.add_sideframe_item(_('Edit Slides'), url=url_change)
        carousel_menu.add_modal_item(_('Add New Slide'), url=url_addnew)
        carousel_menu.add_break()

        url_change = reverse('admin:cms_lab_carousel_carousel_changelist')
        url_addnew = reverse('admin:cms_lab_carousel_carousel_add')
        carousel_menu.add_sideframe_item(_('Edit Carousels'), url=url_change)
        carousel_menu.add_modal_item(_('Add New Carousel'), url=url_addnew)
