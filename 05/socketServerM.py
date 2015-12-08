#!usr/bin/env python

import SocketServer

class myTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print "got connection fron:",self.client_address
        while 1:
            self.data = self.request.recv(8196)
            print self.data
            format_data = "\033[32;1m%s \033[0m" %self.data
            self.request.sendall(format_data.upper())

h,p = '',9999
server = SocketServer.TCPServer((h,p),myTCPHandler)

server.serve_forever()
