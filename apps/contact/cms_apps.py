from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ContactApphook(CMSApp):
    app_name = 'contact'
    name = _('Contact')
    urls = ['contact.urls']

    def get_urls(self, *args, **kwargs):
        return self.urls
