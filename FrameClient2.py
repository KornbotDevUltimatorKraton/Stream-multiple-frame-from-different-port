import cv2
import os
import json
import socket
import pickle
import subprocess
import multiprocessing
import numpy as np
from itertools import count
import threading
import base64
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Client side to receive the command to acticate restart loop
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ("127.0.0.1", 5092)
sock.bind(address)

for tr in count(0):
    data_out, addr = sock.recvfrom(4096)
    data_c = base64.b64decode(data_out, ' /')
    npdata = np.fromstring(data_c, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)
    cv2.imshow("Local image", frame)
    print(frame)  # Getting the string data back
