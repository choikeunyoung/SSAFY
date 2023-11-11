#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "second_practice.settings")
=======
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_practice.settings')
>>>>>>> 4ff1a4d2cac770954257085ccc84c1545f075687
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 4ff1a4d2cac770954257085ccc84c1545f075687
    main()
