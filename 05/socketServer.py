#!/usr/bin/env python
import socket
import time
import os

host = ''
port = 20000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)

while 1:
    conn,addr = s.accept()

    print 'Connection from:',addr
    while 1:
        data = conn.recv(8192)
        if not data:
            print 'Connection lost:',addr
            time.sleep(1)
            break
        else:
            print 'get cmd',data,'on',time.strftime('%y/%m/%d %H:%M:%S')
            cmd = os.popen(data)
            result = cmd.read()
            if result == '': 
                result = 'cmd error!!!'
            result = '\033[32;1mFeedback of the cmd\033[0m\n' + result
            conn.sendall(result)
conn.close()
