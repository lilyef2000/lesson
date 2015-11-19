# -*- coding: utf-8 -*-
#！/usr/bin/env python

while True:
    input = raw_input("请输入你的姓名：")
    if  input == 'lili':
        password = raw_input("请输入你的口令：")      
        p = '1qaz2wsx'
        while password != p:
            if password == 'exit':break            
            print '错误的口令！重试一下吧'
            password = raw_input("请输入你的口令：")            
        else:    
            print '请记住你的信息：'
            print '\n-------------\n'
            print '\t姓名：\t%s\n\t口令：\t%s' %(input,password)
            print '\n-------------\n'
            
            print '口令正确，欢迎登录！\n'
	    while True:
		match_yes = 0
		input = raw_input("\033[32m请输入你想查找的关键字：\033[0m")
		contract_file = file('workers.txt')
		while len(input) == 0 or ' ' in input:
			input = raw_input("\033[32m请输入你想查找的关键字(不要仅输入空格或不输入内容)：\033[0m")
		
		while True:
			line = contract_file.readline()
			if len(line) == 0:break
			if input in line:
			    print '符合要求的条目：\033[36;1m%s\033[0m' % line
			    match_yes = 1
			else:
			    pass
		if match_yes == 0:
			print '没有找到符合要求的条目'

                if input == 'exit':
                    break
            break
    elif input == 'exit':
        break
    else:
        print "对不起，用户%s没找到。" % input
        continue
