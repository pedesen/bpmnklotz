import asyncio

import websockets


bpmn_snapshot_data = """
[
  {
   'id': 0, 
   'type': 'StartEvent', 
   'corners': [
       [414, 505],
       [459, 503],
       [462, 549],
       [416, 550]
    ]
  }, 
  {
   'id': 1, 
   'type': 'ServiceTask', 
   'corners': [
       [414, 505],
       [459, 503],
       [462, 549],
       [416, 550]
    ]
  }, 
  {
   'id': 2, 
   'type': 
   'EndEvent', 
   'corners': [
       [414, 505],
       [459, 503],
       [462, 549],
       [416, 550]
      ]
  }
]
"""


def get_next_bmpn_snapshot():
  return bpmn_snapshot_data


async def bpmn_snapshot_stream(websocket, path):
  while True:
    await websocket.send(get_next_bmpn_snapshot())
    await asyncio.sleep(1)


start_server = websockets.serve(bpmn_snapshot_stream, "127.0.0.1", 5678)


async def hello(websocket, path):
  message = await websocket.recv()
  print(f"Received {message}")

  await websocket.send(bpmn_snapshot_data)
  print(f"> Send bpmn_snapshot")


# start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
