#_*_ coding:utf-8 _*_
#!/usr/bin/env python
import paramiko
import sys,os

host = sys.argv[1]
user = 'antenna'
password = '1qaz2wsx'
pkey_file = '/home/antenna/.ssh/id_rsa'

s = paramiko.SSHClient()  #绑定实例
s.load_system_host_keys() #加载本机HOST文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())


#使用账号密码登录
t = paramiko.Transport((host,22))
#t.connect(username=user,password=password)

#使用key登录，提前使用命令ssh-copy-id -i id_rsa.pub antenna@192.168.1.202将公钥拷贝至远端
key = paramiko.RSAKey.from_private_key_file(pkey_file)
t.connect(username=user,pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/home/antenna/lesson/07/test.txt','test.txt1')
sftp.put('sftp_test.py','/home/antenna/lesson/07/sftp_test.py1')

s.close()
