import strawberry
from strawberry.django import auth
from .types import User, UserInput


@strawberry.type
class AccountQuery:
    my_profile: User = auth.current_user()


@strawberry.type
class AccountMutation:
    login: User = auth.login()
    logout = auth.logout()
    register: User = auth.register(UserInput)
