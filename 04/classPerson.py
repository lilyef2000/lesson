#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class person:
    def __init__(self,nationality):  #类被调用时才执行初始化
        self.country = nationality
        print 'I am being called by an object'
    def info(self,name,age):
        print "you name is %s, and you are %s years old! you are from %s" %(name,age,self.country)
    def skill(self):
        pass
p = person('CN')
p.info('oldboy',35)

