#-*- coding:utf-8 -*-
'''
Created on Aug 24, 2019

@author: jannchan
'''
# some_sentences='''\
# [2019-08-14 04:51:01,986][HTTP报告推送线程 - 192] INFO  - [HttpServer_8888_89] 用户[2019009]推送报文：ReceiveMessageTime = 2019-08-13 07:53:12&Status=Fail&Description=010&FeeCount=2&GatewayId=610660912185348096-115-0&ServiceNo=&Mobile=18077263091&ReportTime=2019-08-14+04%3A50%3A54
# ReceiveMessageTime = 2019-08-13 07:53:12&Status=Fail&Description=010&FeeCount=2&GatewayId=610660912185348096-229-0&ServiceNo=&Mobile=18077683576&ReportTime=2019-08-14+04%3A50%3A54
# [2019-08-14 04:51:05,993][HTTP报告推送线程 - 192] INFO  - [HttpServer_8888_89] 用户[2019009]推送报文：ReceiveMessageTime = 2019-08-13 08:03:18&Status=Fail&Description=702&FeeCount=1&GatewayId=610674931285757952-745-0&ServiceNo=&Mobile=13327368753&ReportTime=2019-08-14+04%3A50%3A59
# '''
  
count = 0
f = open('G:\sentences.txt')
  
Beginstr = "&FeeCount="
Endstr = "&GatewayId"
  
for i in f.readlines():
    if "ReceiveMessageTime = 2019-08-13" in i:
#         stri = str(i)
#         print(stri)
#         fee = stri[stri.index(Beginstr)+10:stri.index(Endstr)]
        fee = i[i.index(Beginstr)+10:i.index(Endstr)]
#         lfee = [int(x) for x in str(fee)]
        print(fee)
#         print (fee)
        count = count+1
        #fee_sum =+ feei
           
    else:
        continue 
     

#print(count)
# print(feei)     
f.close
#===============================================================================
# # content = <div class="a">jb51.net</div> 
# # startStr = <div class="a"> 
# # endStr = </div> 
#  
# def gm(content,a,e):
#     si = content.index(a)
#     if si>=0:
#         si += len(a)
#         ei = content.index(e)
#         return content[si:ei]
#       
# if __name__=='__main__':
#     print(gm('<div class="a">jb51.net</div>','<div class="a">','</div>'))
#===============================================================================

#===============================================================================
# 
# a1 = "Hello.666陈python"
# a2 = "."
# a3 = "th"
#  
# print(a1.index(a2))
# print(a1[:a1.index(a2)])
# print (a1[a1.index(a2):])
# print (a1[a1.index(a2):a1.index(a3)])
#===============================================================================

# num = "132"
# print(map(int,str(num)))
# print([int(x) for x in str(num)])


