"""
ASGI config for second_practice project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "second_practice.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_practice.settings')
>>>>>>> 4ff1a4d2cac770954257085ccc84c1545f075687

application = get_asgi_application()
