# -*- coding: utf-8 -*-
#！/usr/bin/env python

name = raw_input('Name:')
age = int(raw_input('Age:'))
job = raw_input('Job:')
print '---------\n'
print type(age)
print '''\tName: %s
\tAge: %d
\tJob: %s''' %  (name,age,job)
