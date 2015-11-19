#!/usr/bin/python
import tab

contract_file = '01/workers.txt'
f = file(contract_file)
contract_dic = {}

for line in f.readlines():
	name = line.split()[1]
	contract_dic[name] = line

for n,v in contract_dic.items():
	print "%s  \t%s" % (n,v)

while True:
	input = raw_input("Please input the staff name:").strip()
	if len(input) == 0: continue
	if contract_dic.has_key(input):
		print "\033[32;1m%s \033[0m" % contract_dic[input]
	else:
		print "Sorry,no staff name found!"
