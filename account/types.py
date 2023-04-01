import strawberry_django
from strawberry import auto
from django.contrib.auth import get_user_model


@strawberry_django.type(get_user_model())
class User:
    id: auto
    email: auto
    date_joined: auto
    last_login: auto
    is_superuser: auto
    is_staff: auto
    is_active: auto


@strawberry_django.input(get_user_model())
class UserInput:
    email: auto
    password: auto
