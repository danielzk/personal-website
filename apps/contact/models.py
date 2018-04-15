from django.db.models import CharField, EmailField, TextField
from django.utils.translation import ugettext_lazy as _

from utils.models import BaseModel


class Message(BaseModel):
    name = CharField(_('Name'), max_length=255)
    email = EmailField(_('Email'))
    message = TextField(_('Message'))

    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')

    def __str__(self):
        words = self.message.split()
        if len(words) > 10:
            return ' '.join(words[:10]) + ' ...'
        return self.message
