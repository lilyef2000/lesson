#!/usr/bin/env python

import SocketServer

class myMoniterHandler(SocketServer.BaseRequestHandler):
    '''This is the Monitor server'''
    def handle(self):
        recv_data = self.request.recv(1024)
        
        print "From %s: %s" %(self.client_address,recv_data)


if __name__ == "__main__":
    # 该程序是自己主动运行的，而不是作为模块被其他程序调用的
    host.port = '',18000
    server = SocketServer.ThreadingTCPServer((host,port),MyMoniterHandler)
    server.serve_forever()

