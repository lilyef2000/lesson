#!/usr/bin/env python

import tab
import os
ip_file = 'ip.txt'
log_file = '/home/antenna/lesson/06/Ajaxterm-0.10/test.txt'
ip_dic = {}
num = 0
f = file(ip_file)
while True:
	num += 1
	line = f.readline()
	if len(line) == 0 : break
	ip_dic[num] = line
f.close()

while True:
    try:

        for k,v in ip_dic.items():
                print "%s. %s" %(k,v),
        option = int(raw_input('Please choose one server to connect:'))
        if option in ip_dic.keys():
            print ip_dic[option]
            f = file(log_file,'a')
            f.write("\n\nLOGIN INFO:connect to %s" % ip_dic[option])
            f.close()
            user = raw_input('username:').strip()
            cmd = 'ssh %s@%s ' % (user,ip_dic[option])
            os.system(cmd)
        else:
            print 'Number out of range.'
    except ValueError:
        print 'Wrong value'
