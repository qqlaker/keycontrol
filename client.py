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
    print(do, but)
    zmq_socket.send_pyobj((do, but))

main()