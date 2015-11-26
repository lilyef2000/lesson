#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class MyException(Exception):
	pass
try:
	list = ['Alex','Rain','Rachel']
	# list[3]
	raise MyException,"this is my addition data in MyException"
except NameError:
	print 'no this variable'
except MyException,data:
	print 'MyException encountered'
	print data
except : # 无论任何错误均执行该句
	print 'you have an error in your programe'
else:
	print 'No exception'
