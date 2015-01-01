import time
import os
from tkinter import *

def efficiency(x):
	T_I=time.time()
	for i in range(1,x):
		pass
	T_II=time.time()
	return (T_II-T_I)

def efficiency_c(x):
	T_I=time.strftime('%M:%S',time.localtime(time.time()))
	print(T_I)
	for i in range(1,x):
		pass
	T_II=time.strftime('%M:%S',time.localtime(time.time()))
	print(T_II)

def efficiency_avr(x):
#smaller is better
	T_I=time.time()
	for i in range(1,x):
		pass
	T_II=time.time()
	return ((T_II-T_I)/x)


def frequency(x):
#bigger is better
#unit:MHz
	T_I=time.time()
	for i in range(1,x):
		pass
	T_II=time.time()
	return ((1/((T_II-T_I)/x))/1000000)

def frequency_csv(x):
        if os.path.exists(r'D:\XBENCHMARK')==1:
                pass
        else:
                os.mkdir(r'D:\XBENCHMARK')
        T_A=time.time()
        print('Benchmark started at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        file=open(r'D:\XBENCHMARK\result-'+time.strftime('%Y-%m-%d-%H-%M-%S')+'#'+str(int(x))+'.csv','w')
        for ii in range(1000000,1000000+int(x)):
                resultx=frequency(1000000)
                file.write(str(resultx)+'\n')
                #totalmhz+=resultx'D:\XBENCHMARK'
        file.write('##################STATS#################\n')
        file.write('Average:'+','+'=AVERAGE(A1:A'+str(int(x))+')'+',MHz \n')
        #or use this:file.write('Average:,'+str(totalmhz/x)+',MHz')
        file.write('At'+','+time.strftime('%Y-%m-%d-%H:%M:%S')+'\n')
        T_B=time.time()
        print('Benchmark ended at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        file.write('In'+','+str(T_B-T_A)+',secs.')
        file.write('\n########################################')
        file.close()
        print('In '+str(T_B-T_A)+' secs.')
        print('Result saved at:'+'D:\XBENCHMARK')


if __name__=='__main__':
        #num=input('Takes:')
        frequency_csv(1000)
        
#main GUI Programme Part:
#mainwindow=Tk()
#mainwindow.title('X_BENCH_MARK')
#mainwindow.geometry('254x20')
#e=IntVar()
#TAKE_TIMES = Entry(mainwindow,textvariable = e)
#e.set('100')
#TAKE_TIMES.pack(side = RIGHT)
#START_BENCHMARK_BTN=Button(mainwindow,text='Start Benchmark!',command=frequency_csv(e))
#START_BENCHMARK_BTN.pack(fill=BOTH,expand=0)
#mainloop()


