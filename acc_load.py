#1/usr/bin/env python

import pickle

f = open('acc.pkl','r+')
account_info = pickle.load(f)
f.close()

print account_info

account_info['654321'][1] = 20000
account_info['654321'][2] = 200

print account_info

f = open('acc.pkl','w')
pickle.dump(account_info,f)
f.close()


