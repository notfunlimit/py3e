#GNRS=generate result
#Author: XDASADX
#Project name:pyth0n3c1ipse
#e-mail address:leemailbox1@gmail.com

import time
import os
from tkinter import *

loc_addr=os.getcwd()
csv_save_addr=loc_addr+r'\result'

#main
#part I
def frequency(x):
#bigger is better
#unit:MHz        
        T_I=time.time()
        r_num=0
        for i in range(1,x):
                pass
        T_II=time.time()
        return ((1/((T_II-T_I)/x))/1000000)

#part II
def make_csv(x):
        #initial
        total=0

        #create local address
        if os.path.exists(csv_save_addr)==1:
                pass
        else:
                os.mkdir(csv_save_addr)
        
        #start
        T_A=time.time()
        print('Benchmark started at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        file=open(csv_save_addr+'\\result-'+time.strftime('%Y-%m-%d-%H-%M-%S')+'#'+str(int(x))+'.csv','w')
        
        #main
        for ii in range(1,int(x)):
                resultx=frequency(100000)
                file.write(str(resultx)+'\n')
                print(str(ii)+'/'+str(int(x)))
                total+=resultx
        print(str(int(x))+'/'+str(int(x)))
        
        #file feedback
        file.write('#'*40+'\n')
        file.write('Average:'+','+'=AVERAGE(A1:A'+str(int(x))+')'+',MHz \n')
        file.write('At'+','+time.strftime('%Y-%m-%d-%H:%M:%S')+'\n')
        T_B=time.time()
        file.write('In'+','+str(T_B-T_A)+',secs.')
        file.write('\n'+'#'*40)
        file.close()

        #feedback
        print('Benchmark ended at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        print('Result saved at:'+csv_save_addr)
        print('#'*40)
        print('In '+str(T_B-T_A)+' secs.')
        print('Average:'+str(total/int(x))+'MHz')
        print('#'*40)

#part III intitalizing
def intitial(x):
    print('intitalizing...')
    tks=0
    for i in range(1,x):
        tks+=frequency(1000000)
    g_avr=tks/x
    return g_avr


#debug

def deb_inst_avr(x):
    tl=0
    for i in range(1,x):
        tl+=frequency(100000)
    t_a=tl/x
    return t_a

def deb_inst_freq(x):
    for i in range(1,x):
        print(deb_inst_avr(10))
        time.sleep(1)
        os.system('cls')
    print('finished')
