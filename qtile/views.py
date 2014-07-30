import os
import random
import vanilla
from django.conf import settings
from . import models


class Index(vanilla.TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({
            'config_path': os.path.join(settings.PROJECT_DIR,
                'includes/config.py'),
            'screenshots': sorted(models.Screenshot.load(),
                key=lambda x: random.random())[:4],
            'homepage': True,
        })

        return context


class Screenshots(vanilla.TemplateView):
    template_name = 'pages/screenshots.html'

    def get_context_data(self, **kwargs):
        context = super(Screenshots, self).get_context_data(**kwargs)
        context['screenshots'] = models.Screenshot.load()
        return context


class Videos(vanilla.TemplateView):
    template_name = 'pages/videos.html'

    def get_context_data(self, **kwargs):
        context = super(Videos, self).get_context_data(**kwargs)
        context['videos'] = models.Video.raw()
        return context


class Download(vanilla.TemplateView):
    template_name = 'pages/download.html'


class Origins(vanilla.TemplateView):
    template_name = 'pages/origins.html'
