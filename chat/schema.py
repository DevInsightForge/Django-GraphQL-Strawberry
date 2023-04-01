import os
import threading
import strawberry
import asyncio
import asyncio.subprocess as subprocess
import contextlib
from asyncio import streams
from typing import Any, AsyncGenerator, AsyncIterator, Coroutine, List, Optional

from chat.types import ChatRoom, ChatRoomMessage


@strawberry.type
class ChatQuery:
    @strawberry.field
    def hello() -> str:
        return "world"


@strawberry.type
class ChatMutation:
    @strawberry.mutation
    async def send_chat_message(
        self,
        info,
        room: ChatRoom,
        message: str,
    ) -> None:
        ws = info.context.ws
        channel_layer = ws.channel_layer

        await channel_layer.group_send(
            f"chat_{room.room_name}",
            {
                "type": "chat.message",
                "room_id": f"chat_{room.room_name}",
                "message": message,
            },
        )


@strawberry.type
class ChatSubscription:
    @strawberry.subscription
    async def join_chat_rooms(
        self,
        info,
        rooms: List[ChatRoom],
        user: str,
    ) -> AsyncGenerator[ChatRoomMessage, None]:
        """Join and subscribe to message sent to the given rooms."""
        ws = info.context.ws
        channel_layer = ws.channel_layer

        room_ids = [f"chat_{room.room_name}" for room in rooms]

        for room in room_ids:
            # Join room group
            await channel_layer.group_add(room, ws.channel_name)

        for room in room_ids:
            await channel_layer.group_send(
                room,
                {
                    "type": "chat.message",
                    "room_id": room,
                    "message": f"process: {os.getpid()} thread: {threading.current_thread().name}"
                    f" -> Hello my name is {user}!",
                },
            )

        async for message in ws.channel_listen("chat.message", groups=room_ids):
            if message["room_id"] in room_ids:
                yield ChatRoomMessage(
                    room_name=message["room_id"],
                    message=message["message"],
                    current_user=user,
                )
