import os
import yaml
from django.conf import settings


def load_data(name):
    ''' Load a YAML fixture and return the data '''
    path = os.path.join(settings.BASE_DIR, 'data/{0}.yaml'.format(name))
    return yaml.safe_load(open(path, 'r').read())
