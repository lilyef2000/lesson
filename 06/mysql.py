#!/usr/bin/env python

import MySQLdb

try:
    #conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='mysql',port=3306)
    conn = MySQLdb.connect(host='localhost',user='root',passwd='root',port=3306)

    cur = conn.cursor()
    #cur.execute('create database if not exists py_test;')
    #result = cur.fetchall()
    #result = cur.fetchmany(3)
    conn.select_db('py_test')
    #cur.execute('create table host(host varchar(20),user varchar(20),password varchar(30))')
    value = []
    for i in range(1,10):
        ip = '10.0.0.%s' % i
        value.append((i,ip,'antenna','123456'))
    cur.executemany('insert into host values(%s,%s,%s,%s)',value)

    #cur.execute('insert into host values(%s,%s,%s)',value)
    #cur.execute("update host set host='10.0.0.3' where id=3;")
    #cur.execute("alter table  host add id int unsigned auto_increment primary key first;")
    conn.commit()
    result = cur.fetchall()
    
    for r in result:
        print r
    cur.close()
    conn.close()

except MySQLdb.Error,e:
    print 'MySQL Error Msg:',e
