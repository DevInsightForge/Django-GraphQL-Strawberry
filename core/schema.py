# schema.py
import strawberry
import strawberry_django

def get_name() -> str:
    return "Strawberry"


@strawberry.type
class Query:
    name: str = strawberry_django.field(resolver=get_name)

schema = strawberry.Schema(query=Query)