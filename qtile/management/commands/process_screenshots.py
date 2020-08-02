import mimetypes
import os
import tempfile
from PIL import Image
from unipath import Path

from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.files import File
from django.core.management import BaseCommand, CommandError

from qtile import models


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for screenshot in models.Screenshot.load():
            print(screenshot.name)

            # Magic!
            # The thumbnail is only limited by width, so use
            # a larger-than-needed height.
            img = screenshot.img.copy()
            img.thumbnail((200 * screenshot.screens, 1000), Image.ANTIALIAS)

            # Save the thumbnail to a tmpfile
            fd, tmp = tempfile.mkstemp()
            file = os.fdopen(fd, 'w+b')
            type = mimetypes.guess_type(screenshot.name)[0].split('/')[1]
            img.save(file, type)
            file.close()

            # Nuke previous version if it exists
            if staticfiles_storage.exists(screenshot.thumbnail):
                staticfiles_storage.delete(screenshot.thumbnail)

            # save thumbnail to stattic dir
            file = File(open(tmp, 'rb'))
            staticfiles_storage.save(screenshot.thumbnail, file)
            file.close()
            os.unlink(tmp)
