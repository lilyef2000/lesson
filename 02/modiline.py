#_*_ coding:utf-8 _*_
#!/usr/bin/env python
import fileinput

'''
with open('1.txt','r+') as f:
        old = f.read()
	f.seek(0)
	f.write('new line\n'+old)
'''
for line in fileinput.input('1.txt',backup='.bak',inplace = 1):
	line = line.replace('my test string','haha')
        print line
