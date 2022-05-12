# This is client code to receive video frames over UDP
import cv2
import imutils
import socket
from itertools import count
import numpy as np
import time
import base64
import json
import pickle
import threading
BUFF_SIZE = 65536
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host_name = socket.gethostname()
host_ip = '192.168.50.201'  # socket.gethostbyname(host_name)
print(host_ip)
port = 9800
message = b'Hello'
address = "127.0.0.1"
client_socket.sendto(message, (host_ip, port))
fps, st, frames_to_count, cnt = (0, 0, 20, 0)
mem_packet = []


def frame_data():

    packet, _ = client_socket.recvfrom(BUFF_SIZE)
    data = base64.b64decode(packet, ' /')
    npdata = np.fromstring(data, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)
    frame = cv2.putText(frame, 'FPS: '+str(fps), (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    # cv2.imshow("RECEIVING VIDEO",frame)
    # print(frame) # Sending the data in pickle
    mem_packet.append(packet)
    if len(mem_packet) > 1:
        mem_packet.remove(mem_packet[0])


def Frame_main():  # Frame main data
    for r in count(0):
        frame_data()


def Port_test():  # Port main for sending data
    for t in count(0):
        if len(mem_packet) != 0:
            sock1.sendto(mem_packet[0], (address, 5092))


def Port_second():
    for rt in count(0):
        if len(mem_packet) != 0:
            # Sending the json data into the udp
            sock.sendto(mem_packet[0], (address, 5090))


if __name__ == "__main__":
    p1 = threading.Thread(target=Frame_main)
    p2 = threading.Thread(target=Port_test)
    p3 = threading.Thread(target=Port_second)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
