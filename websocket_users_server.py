import asyncio

from websockets import ServerConnection
from websockets.asyncio.server import serve


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    server = await serve(echo, "localhost", 8765)
    await server.wait_closed()


asyncio.run(main())
