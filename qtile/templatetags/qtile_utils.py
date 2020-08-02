from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import resolve, Resolver404

from unipath import Path

register = template.Library()


@register.simple_tag
def active_page(request, view_name):
    if request:
        try:
            return 'active' if resolve(request.path_info).url_name == view_name else ''
        except Resolver404:
            pass
    return ''


@register.simple_tag
def style_tag(path):
    url = staticfiles_storage.url(path)
    if settings.DEBUG:
        return '<link type="text/css" rel="stylesheet/less" href="{0}" />'.format(url)
    return '<link type="text/less" rel="stylesheet" href="{0}" />'.format(url)


@register.simple_tag
def ssi(filename):
    path = settings.PROJECT_DIR.child('includes', filename)
    return open(path, 'r').read()
