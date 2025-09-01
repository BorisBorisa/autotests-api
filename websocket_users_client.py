import asyncio
from websockets.asyncio.client import connect


async def hello():
    uri = "ws://localhost:8765"

    async with connect(uri) as websocket:
        await websocket.send("Привет, сервер!")

        for _ in range(5):
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(hello())
