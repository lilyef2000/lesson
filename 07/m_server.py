#_*_ coding:utf-8 _*_
#!/usr/bin/env python

import SocketServer
import datetime
import pickle

pfile = 'host_dic.pkl'

host_status = {}
f = open('client.txt')
while True:
    line = f.readline().split()
    if len(line)==0:break
    host_status[line[0]] = []
f.close()

class myMoniterHandler(SocketServer.BaseRequestHandler):
    '''This is the Monitor server'''
    def handle(self):
        recv_data = self.request.recv(1024)
        if self.client_address[0] == '192.168.1.201':
            fp = file(pfile,'w')
            pickle.dump(host_status,fp)
            fp.close()
        if self.client_address[0] in host_status.keys():
            host_status[self.client_address[0]].append((datetime.datetime.now(),recv_data))
            print "From %s: %s %s" %(self.client_address,datetime.datetime.now(),recv_data)
        else:
            print "sorry,ip %s is not in the monitor list" % self.client_address[0]
        for t,m in host_status.items():
            print t,m

if __name__ == "__main__":
    # 该程序是自己主动运行的，而不是作为模块被其他程序调用的
    host,port = '',18000
    server = SocketServer.ThreadingTCPServer((host,port),myMoniterHandler)
    server.serve_forever()

