# -*- coding:utf-8 -*-
'''
Created on Aug 22, 2019

@author: chen
'''
# import pandas as pd
# import numpy 
# import re
import traceback

# mydata_csv = pd.read_csv('C:\\test.csv',sep = ',',encoding = 'utf-8')
# mydata_csv

# f = open("E:\Current.log - 副本.2019-08-14")
# line = f.readline()
# while line:
#     print(line, end = '')
#     line = f.readline()
# 
# f.close()

try:
    def readFile():
        readData = []
        count = 0
        Beginstr = "&FeeCount="
        Endstr = "&GatewayId"
        f = open(r"G:\Current.log - 副本.2019-08-14");
        
        
        for i in f.readlines():
    #         if "ReceiveMessageTime = 2019-08-14" in i and "Status=Fail" in i:
            if "ReceiveMessageTime = 2019-08-13" in i:
                fee = i[i.index(Beginstr)+10:i.index(Endstr)]    
    #             lfee = [int(x) for x in str(fee)]          
                stri = str(fee)
                readData.append(stri+'\n')
                count=count+1
                
            else:
                continue
       
        f.close()        
        print("total_line:"+str(count))
        return readData
    
    
    def writeFile():
        data = readFile()
        f = open(r"G:\Chen.txt","w",encoding = 'utf-8')
        f.writelines(data)
        f.close()
     
    if __name__ == '__main__':
        writeFile()


except Exception as e:
    traceback.print_exc(file=open(r'G:\trc.log','w+'))  
else:
    print("Sucess exec.")   
finally:
    print("Done.")

    
    


