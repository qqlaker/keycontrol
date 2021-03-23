"""---Имитация клиента---"""

import sys
import zmq
import datetime
import time

def main():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    do = sys.argv[1]
    but = sys.argv[2]
    zmq_socket.send_pyobj((do, but))


"""# Connection to local server
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    try:
        socket.bind("tcp://*:1337") # instead of '1337' you can put any port
        print('Connected to tcp://*:1337')
    except:
        print('Connection failed')

# Button transmitter
    #while True:
        #msg = str(input('input command: '))
    do = b"test"
    but = 'tab'
    socket.send(do) # this string send msg object on server
    print('Message sent at:', datetime.datetime.now())"""

main()