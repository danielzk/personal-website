from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

MSG_TEMPLATE = """Name: {name}
Email: {email}
Date: {date}

Message:
{message}"""


def on_message_saved(sender, instance, created, **kwargs):
    if created:
        recipients = [email for admin, email in settings.ADMINS]
        send_mail(
            _('NEW MESSAGE - {}').format(settings.PROJECT_DISPLAY_NAME),
            MSG_TEMPLATE.format(
                name=instance.name,
                email=instance.email,
                date=instance.created_at,
                message=instance.message
            ),
            settings.DEFAULT_FROM_EMAIL,
            recipients,
            fail_silently=True,
        )
