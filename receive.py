import socket
import datetime
import pyautogui

size = pyautogui.size()
mousePos = pyautogui.position()
prevMousePos = pyautogui.position()

timeout = 3 #seconds
nextTime = datetime.datetime.now() + datetime.timedelta(seconds=timeout)

# UDP_IP  = '255.255.255.255'
# UDP_IP = '127.0.0.1'
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

# Allow Broadcast
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Bind to any port
sock.bind(('', UDP_PORT))

def checkTimeout():
    now = datetime.datetime.now()
    if now >= nextTime:
        print('timeout!')
        return True
    else:
        return False

# def refreshTimeout():
#     if mousePos != prevMousePos:
#         print('X:', mousePos[0], 'Y:', mousePos[1])
#         nextTime = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
#         prevMousePos = mousePos
#     return


while True:
    if checkTimeout():
        break

    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    mouseStr = data.decode('utf-8')

    mousePos = int(float(mouseStr.split(' ')[1]) * size[0]), int(float(mouseStr.split(' ')[2]) * size[1])
    
    print('X:', mousePos[0], 'Y:', mousePos[1])

    if mousePos != prevMousePos:
        print('X:', mousePos[0], 'Y:', mousePos[1])
        nextTime = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
        prevMousePos = mousePos

    # pyautogui.moveTo(mousePos[0], mousePos[1])

    if mousePos[0] < 10 and mousePos[1] < 10:
        break


