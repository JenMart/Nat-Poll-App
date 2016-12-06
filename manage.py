#!/usr/bin/env python
import os
import sys

# import dbqeury
# import JSONTest

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    # dbqeury.getSnacks()
    from django.core.management import execute_from_command_line
    # JSONTest.pullJSON()
    execute_from_command_line(sys.argv)
