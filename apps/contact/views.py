from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

from .models import Message


class MessageCreate(CreateView):
    model = Message
    fields = ['name', 'email', 'message']
    success_url = reverse_lazy('contact:success')
