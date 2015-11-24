#!/usr/bin/python

def name_info(name,age,job,nationnality='Chinese'):

	print '''%s's information:
	Name:   %s
	Age:    %s
	Job:    %s
        Country:    %s''' % (name,name,age,job,nationnality)	

name_info('Antenna',25,'IT','American')
name_info('Lisa',10,'Student')
