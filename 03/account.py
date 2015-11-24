#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import pickle

#####################################################
# Description: atm程序的帐号信息初始化模块
# Input：初始帐号信息
# Output：字典格式化存储文件acccount.pkl
#####################################################
acccount_info = {'1000000001':['antenna',15000,15000],
	 '1000000002':['lisa'   ,15000,15000]
	} #使用字典数据格式初始化帐号信息

f = file('account.pkl','wb')  #建立文件

pickle.dump(acccount_info,f)  #以字典的形式格式化存储到文件中

f.close()
