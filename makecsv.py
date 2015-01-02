#Author: XDASADX
#Project name:pyth0n3c1ipse
#e-mail address:leemailbox1@gmail.com

import time
import os
from tkinter import *

def frequency(x):
#bigger is better
#unit:MHz        
        T_I=time.time()
        r_num=0
        for i in range(1,x):
                pass
        T_II=time.time()
        return ((1/((T_II-T_I)/x))/1000000)

def make_csv(x):
        #initial
        total=0

        #create address
        if os.path.exists(r'D:\XBENCHMARK\Result')==1:
                pass
        else:
                os.mkdir(r'D:\XBENCHMARK\Result')
        
        #start
        T_A=time.time()
        print('Benchmark started at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        file=open(r'D:\XBENCHMARK\Result\result-'+time.strftime('%Y-%m-%d-%H-%M-%S')+'#'+str(int(x))+'.csv','w')
        
        #main
        for ii in range(1,int(x)):
                resultx=frequency(1000000)
                file.write(str(resultx)+'\n')
                print(str(ii)+'/'+str(int(x)))
                total+=resultx
        print(str(int(x))+'/'+str(int(x)))
        
        #file feedback
        file.write('########################################\n')
        file.write('Average:'+','+'=AVERAGE(A1:A'+str(int(x))+')'+',MHz \n')
        file.write('At'+','+time.strftime('%Y-%m-%d-%H:%M:%S')+'\n')
        T_B=time.time()
        file.write('In'+','+str(T_B-T_A)+',secs.')
        file.write('\n########################################')
        file.close()

        #feedback
        print('Benchmark ended at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        print('Result saved at:'+'D:\XBENCHMARK\Result')
        print('########################################')
        print('In '+str(T_B-T_A)+' secs.')
        print('Average:'+str(total/int(x))+'MHz')
        print('########################################')

if __name__=='__main__':
        #num=input('Takes:')
        make_csv(10000)
