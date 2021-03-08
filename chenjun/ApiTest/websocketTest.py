#coding:utf-8
import websocket
import json

url = 'wss://prosocket.learnta.cn/socket.io/?token=e3662631-195a-3396-8a16-fc42cd91ea35&EIO=3&transport=websocket'
ws = websocket.create_connection(url)
data = {"test":}
ws.send(json.dumps(data))
print(ws.recv())
ws.close()