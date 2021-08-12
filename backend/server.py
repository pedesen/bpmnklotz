import asyncio

import websockets

bpmn_snapshot_data = """
[
  {
   "id": 0, 
   "type": "StartEvent", 
   "corners": [
       [414, 505],
       [459, 503],
       [462, 549],
       [416, 550]
    ]
  }, 
  {
   "id": 1, 
   "type": "ServiceTask", 
   "corners": [
       [414, 505],
       [459, 503],
       [462, 549],
       [416, 550]
    ]
  }, 
  {
   "id": 2, 
   "type": 
   "EndEvent", 
   "corners": [
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
    counter = 0
    while True:
        stream_data = get_next_bmpn_snapshot()
        counter += 1
        print("( %d ) Send stream data: %s" % (counter, stream_data))
        await websocket.send(stream_data)
        await asyncio.sleep(1)


print("Start websocket server on ws://127.0.0.1:5678/")

start_server = websockets.serve(bpmn_snapshot_stream, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
