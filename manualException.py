#!/usr/bin/env python

try:
	list = ['Alex','Rain','Rachel']
	# list[3]
	raise IndexError
except NameError:
	print 'no this variable'
