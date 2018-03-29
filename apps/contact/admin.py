from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'created_at', 'message')

    def get_readonly_fields(self, request, obj=None):
        return self.fields
