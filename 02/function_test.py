#!/usr/bin/env python

def sayHi(name):
	print "Hello \033[32;1m%s\033[0m, how are you?" % name

def info(name,tel):
	print "\033[32;1mName:%s Tel:%s\033[0m" % (name,tel)

with open('01/workers.txt','r') as contact_file:
	for line in contact_file.readlines():
		name =  line.split()[1]
		tel  =  line.split()[3]
		sayHi(name)
		info(name,tel)


