#-*-coding:utf-8-*-
import pymysql
import json

def getConnection():
    return pymysql.connect(host="10.9.184.2", user="KERISAIGDEV", password="WelCome123##", db="KERISAIGDEV", charset="utf8", port=3306)

def getQuestionInfo(lbno, d_type):
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    for i, j in enumerate(lbno):
        lbno[i] = str(j)

    lbno = ", ".join(lbno)
    
    if d_type == 1:
        sql = "SELECT * FROM QUESTIONS WHERE LBNO in ({lbno}) AND DIFFICULTY in (1, 2, 3);".format(lbno=lbno)
    elif d_type == 2:
        sql = "SELECT * FROM QUESTIONS WHERE LBNO in ({lbno}) AND DIFFICULTY in (1, 2, 3, 4, 5);".format(lbno=lbno)
    elif d_type == 3:
        sql = "SELECT * FROM QUESTIONS WHERE LBNO in ({lbno}) AND DIFFICULTY in (3, 4, 5);".format(lbno=lbno)
    
    curs.execute(sql)
    row = curs.fetchall()

    conn.close()

    return row

def getLearningObj(guno):
    conn = getConnection()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    
    lbno = []
    sql = "SELECT LBNO FROM LEARNING_OBJECTIVES WHERE GUNO = {guno} AND ACTIVE = 1;".format(guno=guno)
    curs.execute(sql)
    
    row = curs.fetchall()
    for r in row:
        lbno.append(r["LBNO"])
    
    conn.close()
    
    return lbno
