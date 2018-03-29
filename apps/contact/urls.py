from django.conf.urls import url
from django.views.generic import TemplateView

from .views import MessageCreate

urlpatterns = [
    url(r'^$', MessageCreate.as_view(), name='create'),
    url(r'^success/$',
        TemplateView.as_view(template_name='contact/success.html'),
        name='success'),
]
