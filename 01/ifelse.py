# -*- coding: utf-8 -*-
#！/usr/bin/env python

name = raw_input('Name:')
age = int(raw_input('Age:'))
job = raw_input('Job:')
print '---------\n'
if age < 28:
    print "恭喜，你还是个毛头小伙子！"
elif name == 'lili':
    print "你还有年假可以休，小伙子。"    
else:
    print "老板说：回去上班吧，上有老下有小的"
    
print type(age)
print '''\tName: %s
\tAge: %d
\tJob: %s''' %  (name,age,job)
