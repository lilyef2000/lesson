#!usr/bin/env python

import SocketServer
import os
import time

class myTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "got connection fron:",self.client_address
        while 1:
            self.data = self.request.recv(8196)
            if not data:
                print "connection lost:",self.client_address
                time.sleep(1)
                break
            else:
                print "will run this on server:",self.data,"on",time.strftime('%H:%M:%S')
                cmd = os.popen(self.data)
                if result == '':
                    result = 'cmd error!!!'
                else:
                    result = "\033[32;1m%s \033[0m" %self.data
                self.request.sendall(result.upper())

h,p = '',9999
server = SocketServer.ThreadingTCPServer((h,p),myTCPHandler)

server.serve_forever()
