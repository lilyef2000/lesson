#_*_ coding:utf-8 _*_
#!/usr/bin/python

import pickle

account_info = {
	'123456':['alex',15000,15000],
	'654321':['Big',19000,19000],
}

f = open('acc.pkl','w+')
pickle.dump(account_info,f)
f.close()
