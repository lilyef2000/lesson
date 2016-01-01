#!/usr/bin/env python

import socket
from datetime import datetime
import pickle

def trigger_dump():
    host,port = "192.168.1.201",18000
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    s.connect((host,port))
    s.send("up")

    s.close()


trigger_dump()

f = file('host_dic.pkl','rb')

host_status = pickle.load(f)
f.close()

for h,m in host_status.items():
    if len(m) != 0:
        old_time = m[-1][0]
        time_diff = (datetime.now() - old_time).seconds
        if time_diff > 30:
            print "\033[31;1mNo data received from %s for %s,please check!\033[0m" % (h,time_diff)
        print h,(datetime.now()-old_time).seconds

