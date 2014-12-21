import time
import os

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
        file=open(r'D:\XBENCHMARK\result'+time.strftime('%Y-%m-%d-%H-%M-%S')+'.csv','w')
        for ii in range(1000000,1000000+x):
                resultx=frequency(1000000)
                file.write(str(resultx)+'\n')
                #totalmhz+=resultx
        file.write('Average:'+','+'=AVERAGE(A1:A'+str(x)+')'+',MHz')
        #or use this:file.write('Average:,'+str(totalmhz/x)+',MHz')
        file.close()
        T_B=time.time()
        return 'Finished in '+str(T_B-T_A)+' secs.'
