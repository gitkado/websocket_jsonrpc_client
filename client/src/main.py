import asyncio
import websockets


async def hello():
    # uri = 'ws://websocket-echo.com'
    uri = 'ws://host.docker.internal:8765'
    async with websockets.connect(uri) as websocket:
        await websocket.send('Hello world!')
        print(await websocket.recv())
        # NOTE: Ctrl+Cで終了


asyncio.run(hello())
