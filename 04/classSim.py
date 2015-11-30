#!/usr/bin/env python
#_*_ coding:utf-8 _*_

class Person:
    def __init__(self,name,age,sex,occupation,city,asset=10000):
        self.Name = name
        self.Age = age
        self.Sex = sex
        self.Job = occupation
        self.City = city
        self.Asset = asset

    def tell(self):
        info = '''
        \n\033[33m Hello, my name is %s, I am %s years old, nice to meet you, I am %s, work in %s, How about you!

        \033[0m''' %(self.Name,self.Age,self.Job,self.City)
        print info
        print self.Asset

class Love(Person):
    def __init__(self,name,age,sex,occupation,city,agsset=10000):
        # 继承Person，也可以添加自己的参数，但是继承的参数必须与父类相同
        Person.__init__(self,name,age,sex,occupation,city,agsset)
    def action(self,action_type):
        print action_type
        if action_type == 'FirstMet':
            self.tell()
        if action_type == 'Match=50':
            print 'Bye, do not like each other'
            return 50        
        if action_type == 'WatchMovie':
            pass
        

#P = Person('Bob','36','Male','Advanced System Engineer','Beijing')
p = Love('Bob','36','Male','Advanced System Engineer','Beijing')
r = Love('Bob1','36','Male','Advanced System Engineer','Beijing')


p.action('FirstMet')
if p.action('Match=50') == 50:
    print 'sorry, you are good but not suitable for me!'
    print 'Met R'
    r.action('FirstMet')
