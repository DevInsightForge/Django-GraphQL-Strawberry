# schema.py
import strawberry

from account.schema import AccountMutation, AccountQuery
from chat.schema import ChatMutation, ChatQuery, ChatSubscription


@strawberry.type
class Query(AccountQuery,ChatQuery):
    pass


@strawberry.type
class Mutation(AccountMutation, ChatMutation):
    pass

@strawberry.type
class Subscription(ChatSubscription):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
)
