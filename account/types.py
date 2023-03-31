import strawberry_django
from strawberry import auto
from django.contrib.auth import get_user_model


@strawberry_django.type(get_user_model())
class User:
    username: auto
    email: auto


@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    password: auto
