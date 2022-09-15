import asyncio
import websockets


async def hello():
    uri = 'ws://host.docker.internal:8765'
    async with websockets.connect(uri) as websocket:
        await websocket.send('Hello world!')
        print(await websocket.recv())


asyncio.run(hello())
