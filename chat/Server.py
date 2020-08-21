import basic
import json

def handler(conn, addr, args):
    data = json.loads(basic.recvall(conn))
    if data["type"] == "send":
        pass

    elif data["type"] == "recv":
        pass

server = basic.Server("127.0.0.1", 1337)
server.start(handler, [])