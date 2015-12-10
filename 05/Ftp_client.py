#!/usr/bin/env python

import os
from time import sleep
import user_startup
from socket import *

HOST = '192.168.1.202'
PORT = 21567
BUFSIZ = 4096
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

tcpCliSock.send('auth')
while 1:
    #tcpcliSock.recv(BUFSIZ) == "Username":
    if tcpCliSock.recv(BUFSIZ) == "Username":
        print 'please input your username:'
        while 1:
            data = raw_input('UserName:> ').strip()
            if len(data) == 0:
                continue
            else:
                break
        tcpCliSock.send(data)
        if tcpCliSock.recv(BUFSIZ) == 'correct':
            print 'welcome'
            break
        else:
            print 'Wrong pass'
            continue
while 1:
    data = raw_input('ftp> ').strip()
    if len(data) == 0:
        continue
    elif data == 'quit':
        tcpCliSock.close()
        break
    elif data == 'get' or data == 'send':
        print '\033[31;1mNo file specified,use %s filename \033[0m' % data
        continue
    elif data == 'ls':
        tcpCliSock.send(data)
        file_list = tcpCliSock.recv(8096)
        print file_list
    elif data.split()[0] == 'send':
        try:
            os.stat(data.split()[1])
        except OSError:
            print '\033[31;1mNo file %s found on localhost\033[0m' % data.split()[1]
            continue
        tcpCliSock.send(data)
        print 'send msg:',data
        #tcpCliSock.send('%s\r\n' % data)
        recv_data = tcpCliSock.recv(BUFSIZ)
        if recv_data == 'ok2send':
            file2send = data.split()[1]
            f = open(file2send,'rb')
            file_data = f.read()
            f.close()
            tcpCliSock.sendall(file_data)
            print 'file sent finished!'
            sleep(0.5)
            tcpCliSock.send('file_send_done')
    elif data.split()[0] == 'get':
        tcpCliSock.send(data)
        print 'send msg:',data
        #tcpCliSock.send('%s\r\n' % data)
        recv_data = tcpCliSock.recv(BUFSIZ)
        if recv_data == 'ok2get':
            file2get = "%s" % data.split()[1]
            f = file(file2get,'wb')
            file_get_done_mark = 0
            while 1:
                get_data = tcpCliSock.recv(1024)
                if get_data == 'file_send_to_client_done':
                    file_get_done_mark = 1
                    break
                f.write(get_data)
            f.close()

            if file_get_done_mark == 1:
                print "Download file %s from FTP server success!" % file2get
                continue
            else:
                print 'wrong'
                print 'File %s receive done!' % filename
    elif data == 'help' or data == '?':
        tcpCliSock.send(data)
        help_msg = tcpCliSock.recv(8096)
        print help_msg
 
    else:
        #print 'invalid cmd...'
        tcpCliSock.send(data)
        error_msg = tcpCliSock.recv(8096)
        print 'FTP server:',error_msg

