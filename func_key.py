#_*_ coding:utf-8 _*_
#!/usr/bin/python
# Filename: func_key.py

# 使用关键参数的例子
def func(a,b=5,c=10):
	global abc
	abc =12000000
	print 'a is',a,'and b is',b,'and c is',c
	return a

func(3,7)
func(25,c=24)
e=abc
func(c=50,a=10,b=e)


