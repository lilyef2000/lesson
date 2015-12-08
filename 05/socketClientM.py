#!/usr/bin/env python
import socket
import time

host = '192.168.1.202'
port = 9999 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    INPUT = raw_input("Input:")
    s.send(INPUT)
    received_data = s.recv(8196)
    
    print 'Received from server:\n',received_data,'\non',time.strftime('%y/%m/%d %H:%M:%S')

s.close()
