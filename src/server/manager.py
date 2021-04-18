import asyncio
import datetime
import random
import websockets
from collections import deque
import gameserver
import time
import json

connected = deque()
game = gameserver.gameserver(connected)

connected.appendleft({'websocket':None, 'path':None, 'info':[50,50,2,2,2]})

lastupdate = time.time() 

def encodeJSON(data):
    return json.dumps(data)

async def time(websocket, path):
    global lastupdate
    global connceted
    data = {'websocket':websocket, 'path':path, 'info':[-1,-1,-1,-1,-1]}
    connected.appendleft(data)
    #while True:
    async for message in websocket:
        if("data" in message):
            data['info'] = [int(x) for x in message[6:-1].split(',')]
            #print([int(x) for x in message[6:-1].split(',')])
        if("update" in message):
            game.update()
            await websocket.send("d" + encodeJSON(game.getData(data['info'])))
        if("obstacles" in message):
            await websocket.send("o" + encodeJSON(list(game.obstacles)))
        #if("user" in message):
        #    await websocket.send("u" + encodeJSON(data['info']))
        #now = datetime.datetime.utcnow().isoformat() + 'Z'
        #await websocket.send(now)
        #await asyncio.sleep(random.random() * 3)
        
        #print(data)
    #while True:
        #now = datetime.datetime.utcnow().isoformat() + 'Z'
        #await websocket.send(now)
    #    await asyncio.sleep(random.random() * 3)
        #print('test')
        #print(time.time())
        #if (time.time() - lastupdate == 6000):
        #    print('test')
        #    print(lastupdate)
        #    lastupdate = time.time()


start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

#while True:
#    print('test')
