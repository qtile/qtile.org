#!/usr/bin/env python
import os
import pprint
import sys

import dotenv

if __name__ == "__main__":
    # Run output through the pretty printer.
    sys.displayhook = pprint.pprint

    # Load our .env
    dotenv.load_dotenv(dotenv.find_dotenv())

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qtile.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
