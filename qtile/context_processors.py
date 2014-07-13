from django.views.debug import get_safe_settings


def settings(request):
    return {
        'settings': get_safe_settings(),
    }
