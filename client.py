"""---Имитация клиента---"""

import zmq
import datetime

def main():
# Connection to local server
    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    try:
        socket.bind("tcp://*:1337") # instead of '1337' you can put any port
        print('Connected to tcp://*:1337')
    except:
        print('Connection failed')

# Button transmitter
    while True:
        msg = str(input('input command: '))
        socket.send_string(msg) # this string send msg object on server
        print('Message sent at:', datetime.datetime.now())


if __name__ == '__main__':
    main()