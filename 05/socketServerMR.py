#!/usr/bin/env python

import SocketServer

class myTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(4096)
        print self.data
        format_data = "\033[32;1m%s\033[0m" % self.data
        self.request.sendall(format_data.upper())

h,p = '',20000
server = SocketServer.TCPServer((h,p),myTCPHandler)

server.serve_forever()
