#!/usr/bin/env python
import socket
import time

host = '192.168.1.7'
port = 18000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while 1:
    INPUT = raw_input("Input your cmd:")
    s.send(INPUT)
    received_data = s.recv(1024)
    
    print 'Received from server:',received_data,'on',time.strftime('%y/%m/%d %H:%M:%S')

s.close()