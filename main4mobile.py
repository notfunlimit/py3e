import time

def frequency(x):
#bigger is better
#unit:MHz
	T_I=time.time()
	for i in range(1,x):
		pass
	T_II=time.time()
	return ((1/((T_II-T_I)/x))/1000000)



def make_csv(x):
        #initial
        total=0
        T_A=time.time()
        #main
        for ii in range(1,int(x)):
                resultx=frequency(1000000)
                print str(ii)+'/1000'
                total+=resultx

        #handle result in file
        print total/x




        
#prog_conse=Tk()
#prog_conse.title('Processing...')
#prog_conse.geometry('254x20')
#labelproc = Label(prog_conse,text = 1)
#labelproc.pack(fill=BOTH,expand=0)
#mainloop()

make_csv(100)




