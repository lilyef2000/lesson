#!/usr/bin/env python
import time,sys

dict = {0:0,1:1,2:2,3:3,4:4,5:5,6:6}
input = int(raw_input('please input number:'))
for num in range(input):
	try:
		print "number %s" % dict[num]
		time.sleep(0.5)
	except KeyError:
		print '%s not exist' % num
		break
	except KeyboardInterrupt:
		print 'do not input ctrl + c'
		sys.exit()
	finally:
		print 'I am going to run this code before exit'