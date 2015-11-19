#_*_ coding:utf-8 _*_
#!/usr/bin/python
import sys

f = file('1.txt')
products = []
prices = []
shop_list = []
for line in f.readlines():
	new_line = line.split()
	#print new_line
	products.append(new_line[0])
	prices.append(int(new_line[1]))

print products
print prices

salary = int(raw_input('Please input your salary:'))
while True:
	print 'Welcom,things you can buy as below:'
	for p in products:
		p_index = products.index(p)
		p_price = prices[p_index]
		print p,p_price
	choice = raw_input('Please input what you want to buy:')
	f_choice = choice.strip()
	if f_choice in products:
		print '\033[36;1mYes,it is in the list.\033[0m'	
		f_index = products.index(f_choice)
		f_price = prices[f_index]
		if salary >= f_price:
			print '\033[36;1mCongratulations,%s added to your shop list.\033[0m' % f_choice
			shop_list.append(f_choice)
			salary = salary - f_price
			print "'\033[36;1mNow.you have %d left! keep buying!\033[0m'" % salary
		else:
			if salary < min(prices):
				print "\033[36;1mYou can't buy anything! Bye!\033[0m"
				print "You have bought:%s" % shop_list
				sys.exit()
			else:
				print "'\033[36;1mSorry,money is not enough to buy %s,please try another one.\033[0m'" % f_choice
			
			
	else:
		print '\033[36;1mSorry,%s is not in the list,try another one.\033[0m' % f_choice


	
