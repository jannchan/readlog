# -*- coding:utf-8 -*-
'''
Created on Aug 23, 2019
dddjj
@author: chen
'''
from pymongo import MongoClient
import pymongo
import datetime
import string
import traceback

try:
    conn = MongoClient('192.168.176.92',27017)
    db = conn.UMP
    col = db.Message
    
    # print(col.find().count())
    # print(col.find({"sender": "2019007",
    #                 "receiveMessageTime":{"$gt":"2019-08-21 0:0:0","$lt":"2019-08-21 23:59:59"}
    #                 }).count())
    
    date =datetime.date.today()
    # print(date)         
    
    start_time = str(date)+" 00:00:00"
    end_time = str(date)+" 23:59:59"
    match = {
            'receiveMessageTime': {
            '$gte': start_time,
            '$lte': end_time
            }   }
    
    groupby = 'sender'
    group = {
        '_id': "$%s" % (groupby if groupby else None),
        'count': {'$sum': 1}    }
    
    ret = col.aggregate(
        [
            {'$match': match},
            {'$group': group}
        ]   )
    
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = open('E:\mongopy.txt','w')
    f.write('查询时间：' + nowTime + '\n' )
    # print(ret)
    
    for a in ret:
        b = ret[a]
    #     print(b)
        if isinstance(b,list):
            c = b
    #         print(c)
            for d in c:
                e = str(d)
    #             print(d)
                f.write(e + '\n' )
                
    f.close()
    
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("查询完成：" + nowTime)            


except Exception as e:
    traceback.print_exc(file=open(r'G:\trc.log','w+'))   
else:
    print("Sucess exec.")   
finally:
    print("Done.")
    db.close()
    conn.close()
    
                
        
