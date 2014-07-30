import os
import yaml
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.images import ImageFile
from unipath import Path


class Model(object):
    order = None

    def __init__(self, data):
        self._data = data

    def __getattr__(self, key):
        try:
            return self._data[key]
        except KeyError:
            raise AttributeError

    @classmethod
    def raw(cls):
        ''' Load a YAML fixture and return the raw data '''
        path = os.path.join(settings.BASE_DIR, 'data/{0}.yaml'.format(cls.__name__))
        results = yaml.safe_load(open(path, 'r').read())
        return results

    @classmethod
    def load(cls):
        ''' Load the data and return a list of model instances '''
        results = [cls(item) for item in cls.raw()]
        if cls.order:
            results.sort(key=lambda i: getattr(i, cls.order))
        return results


class Screenshot(Model):
    order = 'image'

    @property
    def image(self):
        return Path(self._data['image'])

    @property
    def path(self):
        return Path(staticfiles_storage.path(self.image))

    @property
    def file(self):
        path = staticfiles_storage.path(self.image)
        return ImageFile(open(path))

    @property
    def screens(self):
        if self.file.width / self.file.height > 1:
            return 2
        return 1

    @property
    def thumbnail(self):
        return Path(self.image.parent, 'thumb', self.image.name)


class Video(Model):
    pass
