#!usr/bin/env python

import SocketServer
import os
import time

class myTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "got connection fron:",self.client_address
        while 1:
            self.data = self.request.recv(8196)
            if not self.data:
                print "connection lost:",self.client_address
                time.sleep(1)
                break
            else:
                print "will run \033[32;1m%s:%s\033[0m on server:" %(self.client_address,self.data),"on",time.strftime('%H:%M:%S')
                cmd = os.popen(self.data.strip())
                result = cmd.read()
                if result == '':
                    result = 'cmd error!!!'
                result = "\033[32;1m%s\033[0m" %result
                self.request.sendall(result)

h,p = '',9999
server = SocketServer.ThreadingTCPServer((h,p),myTCPHandler)

server.serve_forever()
