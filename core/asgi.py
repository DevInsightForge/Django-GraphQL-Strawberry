"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

"""

import os

from strawberry.channels import GraphQLProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django_asgi = get_asgi_application()

from core.schema import schema

application = GraphQLProtocolTypeRouter(
    django_application=django_asgi,
    schema=schema,
)
