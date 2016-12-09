#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

# from polls import dbqeury

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    # dbqeury.getSnacks()
    execute_from_command_line(sys.argv)
