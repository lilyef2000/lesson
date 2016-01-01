import socket
import time

host,port = "192.168.1.201",18000
while True:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    s.connect((host,port))
    s.send("up")

    s.close()

    time.sleep(30)
