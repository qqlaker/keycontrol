"""---Overlord---"""

import keyboard
import zmq

def main():

# Connection to local server
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
        msg = socket.recv_string() # take last message from server
        list = msg.split(' ')
        if len(list) < 2 or len(list) > 2:
            pass
        elif list[0] == 'press':
            try:
                keyboard.press(list[1])
            except:
                print('Unexpected button')
        elif list[0] == 'release':
            try:
                keyboard.release(list[1])
            except:
                print('Key', '[' + list[1] + ']', 'was not pressed')


if __name__ == '__main__':
    main()


