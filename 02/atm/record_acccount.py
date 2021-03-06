#_*_ coding:utf-8 _*_
#!/usr/bin/env python
import pickle
import time,logger
import sys

#####################################################
# Description: atm程序的帐户消费模块
# Input：
# Output：
#####################################################

# 读入文件中存储的字典信息
pkl_file = open('account.pkl','rb')
account_list = pickle.load(pkl_file)
pkl_file.close()

# 
def recon(account,cost_amount,expense_type):
	# 使用读写模式重新打开格式化存储文件
	pkl_file = open('account.pkl','wb')
	old_position = account_list[account][2] # 获取账户的可用余额
	global intrest
	intrest = 0	

	if old_position < cost_amount:
		print '余额不足！'
		pickle.dump(account_list,pkl_file) # 将账户新的余额格式化写入pkl文件
	        pkl_file.close()
		return False
	else:
		if expense_type == 'Withdraw':
			intrest = cost_amount * 0.05

		new_position = old_position - cost_amount - intrest # 花掉后的余额
		account_list[account][2] = new_position # 新的余额写入字典
		print new_position # 打印出来看看
		pickle.dump(account_list,pkl_file) # 将账户新的余额格式化写入pkl文件
		pkl_file.close()
		return True

print account_list

# recon('1000000001',500)
# logger.record_log('1000000001',500,'Adidas')

if recon('1000000001',800,'Withdraw'):
	logger.record_log('1000000001',800,'Withdraw',intrest)
else:
	logger.record_log('1000000001',0,'Withdraw failure!!!',0)
