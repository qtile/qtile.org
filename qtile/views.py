import os
import random
import vanilla
from django.conf import settings
from .utils import load_data


class Index(vanilla.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({
            'config_path': os.path.join(settings.PROJECT_DIR,
                'includes/config.py'),
            'screenshots': sorted(load_data('screenshots'),
                key=lambda x: random.random())[:5],
            'homepage': True,
        })

        return context


class Screenshots(vanilla.TemplateView):
    template_name = 'pages/screenshots.html'

    def get_context_data(self, **kwargs):
        context = super(Screenshots, self).get_context_data(**kwargs)
        context['screenshots'] = load_data('screenshots')
        return context


class Videos(vanilla.TemplateView):
    template_name = 'pages/videos.html'

    def get_context_data(self, **kwargs):
        context = super(Videos, self).get_context_data(**kwargs)
        context['videos'] = load_data('videos')
        return context


class Download(vanilla.TemplateView):
    template_name = 'pages/download.html'
