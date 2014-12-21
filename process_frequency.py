import time

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
        file=open(r'C:\result.csv','w')
        for ii in range(1000000,1000000+x):
                resultx=str(frequency(ii))
                file.write(resultx+'\n')
        file.write('Average:'+','+'=AVERAGE(A1:A'+str(x)+')')
        file.close()
        return 'finished'



