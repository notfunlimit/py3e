import time
import os
from tkinter import *
import threading

def frequency(x):
#bigger is better
#unit:MHz
	T_I=time.time()
	for i in range(1,x):
		pass
	T_II=time.time()
	return ((1/((T_II-T_I)/x))/1000000)



def make_csv(x):

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
                print(str(ii)+'/1000')

        #handle result
        file.write('##################STATS#################\n')
        file.write('Average:'+','+'=AVERAGE(A1:A'+str(int(x))+')'+',MHz \n')
        file.write('At'+','+time.strftime('%Y-%m-%d-%H:%M:%S')+'\n')
        T_B=time.time()
        print('Benchmark ended at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        file.write('In'+','+str(T_B-T_A)+',secs.')
        file.write('\n########################################')
        file.close()

        #feedback
        print('In '+str(T_B-T_A)+' secs.')
        print('Result saved at:'+'D:\XBENCHMARK\Result')

if __name__=='__main__':
        #num=input('Takes:')
        make_csv(1000)


