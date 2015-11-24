#!/usr/bin/python
## this is a program for recording logs,the simple usage as below:
#  author: antenna
#  last update: 2015.11.24
#  version: 1.0

import time
logfile = 'backup.log'

def record_log(Backup_type,Status,files,description = 'NULL'):
	date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	record_line = "%s    %s    %s    %s    %s\n" % (date,Backup_type,Status,files,description)
	f = file(logfile,'a')
	f.write(record_line)
	f.flush()
	f.close()
