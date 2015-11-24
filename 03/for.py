#!/usr/bin/env python
import time

for i in range(1,101):
	try:
		print 'Number %s' %i
		time.sleep(0.5)
	except KeyboardInterrupt:
		print 'doing'
		continue
	
