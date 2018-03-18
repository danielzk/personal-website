from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def get_tree_spacer(item):
    return mark_safe('<span class="tree-spacer"></span>' * (item.get_depth() - 1))


@register.simple_tag()
def get_depth_spacer(item):
    return mark_safe(item.get_depth() - 1)
