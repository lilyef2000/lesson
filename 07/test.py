#_*_ coding:utf-8 _*_
#!/usr/bin/env python
import paramiko
import sys,os

host = sys.argv[1]
user = 'antenna'
password = '1qaz2wsx'
pkey_file = '/home/antenna/.ssh/id_rsa'

cmd = sys.argv[2]

s = paramiko.SSHClient()  #绑定实例
s.load_system_host_keys() #加载本机HOST文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())


#使用账号密码登录
#s.connect(host,22,user,password,timeout=5) #连接远程主机
#stdin,stdout,stderr = s.exec_command(cmd)  #执行命令

#使用key登录，提前使用命令ssh-copy-id -i id_rsa.pub antenna@192.168.1.202将公钥拷贝至远端
#key = paramiko.RSAKey.from_private_key_file(pkey_file)
#s.connect(host,22,user,pkey=key,timeout=5)

if sys.argv[3] == 'KEY':
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s.connect(host,22,user,pkey=key,timeout=5)

elif sys.argv[3] == 'PASSWORD':
    s.connect(host,22,user,password,timeout=5) #连接远程主机

stdin,stdout,stderr = s.exec_command(cmd)
cmd_result = stdout.read(),stderr.read() #读取命令结果

for line in cmd_result:
    print line,

s.close()
