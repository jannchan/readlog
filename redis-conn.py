# -*- coding:utf-8 -*-
'''
Created on Aug 22, 2019

@author: chen
'''

from rediscluster  import RedisCluster
# 使用默认方式连接到数据库
startup_node = [{"host": "10.1.49.237", "port": "7001"},
                {"host": "10.1.49.239", "port": "7003"},
                {"host": "10.1.49.239", "port": "7006"},
                {"host": "10.1.49.237", "port": "7008"}]
#startup_nodes = [{"host": "10.1.105.146", "port": "7003"},{"host": "10.1.105.145", "port": "7005"},{"host": "10.1.105.146", "port": "7006"},{"host": "10.1.105.144", "port": "7008"}]
rc = RedisCluster(startup_nodes=startup_node, 
                  decode_responses=True,
                  readonly_mode=True)
# rc.set('chen', "chen.cc")
# print(redis.VERSION)
# print(rc.hgetall('MessageWaitingReport_20190821_02'))
# print(rc1.hget(name = 'MessageWaitingReport_20190821_02',key='CMPPClient_dx_95567:-8455503350619681570' ) )
# print(rc.keys())
# print(rc.dbsize())
# print(rc.hmget(name="*MessageWaitingReport*",keys="*SME*"))
# print(rc.hscan("*MessageWaitingReport*"))
rc_key = rc.keys()
rc_db = rc.dbsize()


for i in rc_key:
    rc_i = i.find('MessageWaitingReport')
    print(rc.hgetall(rc_i))

# for b,d in rc_db:
#     print(b,d)
