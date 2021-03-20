import zmq
import time
import datetime

def main(who):

    ctx = zmq.Context()
    socket = ctx.socket(zmq.PUB)
    socket.bind("tcp://*:1337")

    while True:
        msg = input("%s> " % who)
        socket.send_pyobj((msg, who))
        print(datetime.datetime.now())

if __name__ == '__main__':
    import sys
    ad = 'tcp://localhost:1337'
    who = 'Michael'
    main(who)

"""key = ''
message = ''
who = 'Michael'

time.sleep(1)
print('Connecting to server')
context = zmq.Context()
socket = context.socket(zmq.REQ)
try:
    socket.connect('tcp://localhost:1337')
    print('Connected at:', datetime.datetime.now())
except:
    print('Error')

while True:
    msg = str(input('%s> ' % who))
    socket.send_pyobj((msg, who))"""