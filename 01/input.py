# -*- coding: utf-8 -*-
#！/usr/bin/env python


while True:
    input = raw_input("请输入你的姓名：")
    if  input == 'lili':
        password = raw_input("请输入你的口令：")      

        p = '1qaz2wsx'
        while password != p:
            print '错误的口令！重试一下吧'
            password = raw_input("请输入你的口令：")
        else:
            print '请记住你的信息：'
            print '\n-------------\n'
            print '\t姓名：\t%s\n\t口令：\t%s' %(input,password)
            print '\n-------------\n'
            
            print '口令正确，欢迎登录！\n'
            break       
    else:
        print "对不起，用户%s没找到。" % input
        continue
        
    
