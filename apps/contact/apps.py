from django.apps import AppConfig
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class ContactConfig(AppConfig):
    name = 'contact'
    verbose_name = _('Contact')

    def ready(self):
        from .models import Message
        from .signals import on_message_saved
        post_save.connect(on_message_saved, sender=Message)
