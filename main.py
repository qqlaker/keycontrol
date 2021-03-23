"""---Overlord---"""

import keyboard
import zmq

def main():
    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect('tcp://127.0.0.1:5557')
    while True:
        work = consumer_receiver.recv_pyobj()
        print(work[0], work[1])

""" Connection to local server
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.setsockopt_string(zmq.SUBSCRIBE, "")
    try:
        socket.connect("tcp://localhost:1337") # instead of '1337' you can put any port
        print('Connected to tcp://localhost:1337')
    except:
        print('Connection failed')

# Requests handler
    while True:
        msg = socket.recv_pyobj() # listen last message from server
        print(msg)
        if len(msg) < 2 or len(msg) > 2:
            pass
        elif msg[0] == 'press':
            try:
                keyboard.press(msg[1])
                print('pressed')
            except:
                print('Unexpected button')
        elif msg[0] == 'release':
            try:
                keyboard.release(msg[1])
                print('released')
            except:
                print('Key', '[' + msg[1] + ']', 'was not pressed')
        else:
            print(msg[1])"""


if __name__ == '__main__':
    main()


