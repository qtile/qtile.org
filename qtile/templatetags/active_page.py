from django import template
from django.core.urlresolvers import resolve, Resolver404

register = template.Library()


@register.simple_tag
def active_page(request, view_name):
    if request:
        try:
            return 'active' if resolve(request.path_info).url_name == view_name else ''
        except Resolver404:
            pass
    return ''
