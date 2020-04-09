import socket
import pyautogui
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

size = pyautogui.size()

# UDP_IP  = '255.255.255.255'
# UDP_IP = '127.0.0.1'
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

sock.bind(('', UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    mouseStr = data.decode('utf-8')
    mousePos = int(float(mouseStr.split(' ')[1]) * size[0]), int(float(mouseStr.split(' ')[2]) * size[1])
    
    print('X:', mousePos[0], 'Y:', mousePos[1])    
    # print(mousePos[0] + mousePos[1])    

    pyautogui.moveTo(mousePos[0], mousePos[1])

    # Exit condition
    if mousePos[0] < 10 and mousePos[1] < 10:
        break
