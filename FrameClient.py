import cv2
import os
import json
import socket
import pickle
import subprocess
import multiprocessing
import numpy as np
from itertools import count
import base64
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Client side to receive the command to acticate restart loop
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ("127.0.0.1", 5090)
sock.bind(address)

# username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer
# Getusername = username.split("-")[0].split(" ")[1]  #Get the username
#HOME_PATH = "/home/"+str(Getusername)+"/Automaticsoftware/"
# running the downloader application to start and reset the loop download
#print("Start downloader from request")
#os.system("python3 "+HOME_PATH+"tibreakout_control_download.py")
for tr in count(0):
    data_out, addr = sock.recvfrom(4096)
    data_c = base64.b64decode(data_out, ' /')
    npdata = np.fromstring(data_c, dtype=np.uint8)
    frame = cv2.imdecode(npdata, 1)
    print(frame,type(data_out))
    #print(frame)  # Getting the string data back
    # Sending the json data into the udp
    #sock.sendto(, (address, 5092))
    # if data.decode() == "Finished Downloading":
    #           print("Restart software")
    #           os.system("python3 "+HOME_PATH+"tibreakout_control_download.py")
    #received  = pickle.loads(data)
    #message = json.loads(received)
    # print(received,type(received),addr)
    # print(message,type(message),addr)
