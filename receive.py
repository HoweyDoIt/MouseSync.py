import socket
import pyautogui
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

size = pyautogui.size()

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    mouseStr = data.decode('utf-8')
    mousePos = mouseStr.split(" ")
    
    print("X:", mousePos[0], "Y:", mousePos[1])    

    # Exit condition
    if mousePos[0] < 0.05 and mousePos[1] < 0.05:
        break
