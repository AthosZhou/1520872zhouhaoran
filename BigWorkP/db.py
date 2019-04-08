import sqlite3

conn=sqlite3.connect('./athos.sqlite')
cur=conn.cursor()

def isExist(username,password):
    sql="select * from main.users where username='%s' and pwd='%s'" %(username,password)
    result=cur.execute(sql).fetchall()
    if(len(result)):
        return True
    else:
        return False
    conn.close()

def havsExist(username):
    sql="select * from users where username='%s'" %(username)
    result = cur.execute(sql).fetchall()
    if (len(result)):
        return True
    else:
        return False
    conn.close()


def adduser(username,password):
     sql="insert into users(username, pwd) values('%s','%s')" %(username,password)
     cur.execute(sql)
     conn.commit()
     conn.close()

def allthinks():
    sql="select * from thinks"
    result = cur.execute(sql).fetchall()
    return  result
    conn.close()

def histhink(username):
    sql="select * from thinks where username='%s'" %(username)
    result = cur.execute(sql).fetchall()
    return result
    conn.close()
