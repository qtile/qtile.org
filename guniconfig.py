import os
import sys


def when_ready(server):
    dir = os.path.dirname(os.path.abspath(__file__))
    if dir not in sys.path:
        sys.path.append(dir)

    from django.core.management import call_command
    call_command('validate')
