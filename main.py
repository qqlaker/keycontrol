"""---Overlord---"""

import keyboard
import zmq
import time

def main():
    context = zmq.Context()
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect('tcp://127.0.0.1:5557')
    while True:
        msg = consumer_receiver.recv_pyobj()
        if len(msg) < 2 or len(msg) > 2:
            pass
        elif msg[0] == 'press':
            keyboard.press(msg[1])
        elif msg[0] == 'release':
            keyboard.release(msg[1])
        else:
            pass

if __name__ == '__main__':
    main()


