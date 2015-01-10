#Main module of this program
#GNRS=generate result
#Author: XDASADX
#Project name:pyth0n3c1ipse
#e-mail address:leemailbox1@gmail.com

#import modules
import time
import sys
import os
from tkinter import *

local_addr=''.join((list(os.getcwd())[:-4]))
sys.path.append(local_addr)

#import adsys
import run

loc_addr=os.getcwd()
csv_save_addr=loc_addr+r'\result'


#main
#part I
def frequency(x):
#bigger is better
#unit:MHz        
        T_I=time.time()
        r_num=0
        for i in range(0,x):
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
        for ii in range(0,int(x)):
                resultx=frequency(100000)
                file.write(str(resultx)+'\n')
                print(str(ii)+'/'+str(int(x)))
                total+=resultx
        print(str(x)+'/'+str(x))
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
        return total/(int(x))

#part III intitalizing
def intitial(x):
    print('intitalizing...')
    tks=0
    for i in range(0,x):
        tks+=frequency(1000000)
    g_avr=tks/x
    return g_avr


#debug

def deb_inst_avr(x):
    tl=0
    for i in range(0,x):
        tl+=frequency(100000)
    t_a=tl/x
    return t_a

def deb_inst_freq(x):
    for i in range(0,x):
        print(deb_inst_avr(10))
        time.sleep(1)
        os.system('cls')
    print('finished')

#GUI FUNCTIONS
def wait_n_clear(x,textbox):
    time.sleep(x)
    textbox.delete(0.0, END)
    

def rproc():
    run.mcsv_run()
    info_src.insert(1.0,'Finished')
    info_src.update()
    wait_n_clear(2,info_src)

#GUI FRAME
frame_main=Tk()
frame_main.iconbitmap('res/icon/ICO_32x32.ico')
frame_main.title("Pyth0n3c1ipse")
frame_main.geometry('256x32')
frame_main.resizable(False, False)



process = Button(frame_main,text='RUN_BENCHMARK',command=rproc,activeforeground='navy',activebackground='white')
process.pack(fill=Y,side='right')

info_src=Text(frame_main,fg='midnight blue')
info_src.pack(side='left',fill=X)

mainloop()
