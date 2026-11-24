import json
import zmq

# Small Microservice Communication
# Statistics getting those values.
def communicationsOut(tableStored):
    sentOut = {
        "values": tableStored,
        "stats": ["mean", "median", "mode", "max", "min", "unique"]
    }

    convertedJSON = json.dumps(sentOut)
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    socket.send_string(convertedJSON)
    recJSON = socket.recv_string()
    convertedJSON = json.loads(recJSON)
    socket.close()
    context.term()
    return convertedJSON