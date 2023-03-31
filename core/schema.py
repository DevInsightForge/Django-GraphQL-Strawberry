# schema.py
import strawberry

from account.schema import AccountMutation, AccountQuery


@strawberry.type
class Query(AccountQuery):
    pass


@strawberry.type
class Mutation(AccountMutation):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
