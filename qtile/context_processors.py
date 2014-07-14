from django.conf import settings
from django.views.debug import get_safe_settings


def context(request):
    return {
        'debug': settings.DEBUG,
        'settings': get_safe_settings(),
    }
