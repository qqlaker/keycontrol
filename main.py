import time
import keyboard
import threading
import sys
import datetime
import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    print("Connecting to: ", "tcp://localhost:1337")
    socket.connect("tcp://localhost:1337")

    while True:
        msg = socket.recv_pyobj()
        print("%s: %s" % (msg[1], msg[0]), datetime.datetime.now())


if __name__ == '__main__':
    import sys
    main()

"""def connect():
    global socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    try:
        socket.bind("tcp://*:1337")
        print('Server started at: ', datetime.datetime.now())
    except:
        print('Error')

def main():
    b = True
    key = ''
    msg = ''
    while True:
        msg = socket.recv_pyobj()
        print("%s: %s" % (msg[1], msg[0]))
    while True:
        key = socket.recv()
        key = key.decode('utf-8')
        print("key:", key, "pressed at:", datetime.datetime.now())
        socket.send(b'Answ')

if __name__ == '__main__':
    connect()
    main()"""



