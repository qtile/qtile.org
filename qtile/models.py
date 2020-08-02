import os
import yaml

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files.images import ImageFile
from django.utils.functional import cached_property

from PIL import Image
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
    order = 'name'

    def __init__(self, data):
        super().__init__(data)
        self._data['image'] = Path(self._data['image'])
        print(self.name, self.screens)

    @cached_property
    def img(self):
        img = Image.open(self.path)
        if img.mode not in ('L', 'RGB'):
            img = img.convert('RGB')
        return img

    @cached_property
    def path(self):
        return Path(staticfiles_storage.path(self.image))

    @cached_property
    def name(self):
        return self.path.name

    @cached_property
    def file(self):
        path = staticfiles_storage.path(self.image)
        return ImageFile(open(path))

    @cached_property
    def screens(self):
        if (self.img.width / self.img.height) > 2:
            return 2
        return 1

    @cached_property
    def thumbnail(self):
        return Path(self.image.parent, 'thumb', self.name)


class Video(Model):
    pass
