#!/usr/bin/env python
import time

dict = {0:0,1:1,2:2,3:3,4:4,5:5,6:6}
input = int(raw_input('please input number:'))
try:
	for num in range(input):
		try:
			print "number %s" % dict[num]
			time.sleep(0.5)
		except KeyboardInterrupt:
			print 'do not input ctrl + c'
except KeyError:
	print '%s not exist' % num
