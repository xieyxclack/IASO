__author__ = 'PrlNcE'
# coding: utf-8

import MySQLdb

def getAll():
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='test',port=3306,charset='utf8')
        cur=conn.cursor()
        res = cur.execute('select * from alias_wash1')
        res = cur.fetchall()
        #for i in res:
        #    print i[0],i[1]


        cur.close()
        conn.close()
        return res
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
