#Followed GPL v3 License
#github webpage:https://github.com/XDASADX/Pyth0n3c1ipse
#compiler: sublime 2 & Python IDLE
#contributor: XDASADX leemailbox1@gmail.com
#            

#import system modules
import sys
import os
import time
from tkinter import *

#generate local address
loc_addr=os.getcwd()
sys.path.append(loc_addr)
import adsys

adsys.add_sys()

#import functions
import run

#main
if __name__ == '__main__':

    frame_main=Tk()
    frame_main.iconbitmap('res/icon/ICO_32x32.ico')
    frame_main.title("Pyth0n3c1ipse")
    frame_main.geometry('256x32')
    frame_main.resizable(False, False)
    def rproc():
    	run.mcsv_run()
    	for i in range(0,200):
    		status=Label(frame_main,text=str(i)+'/'+'200')
    		status.pack(fill=X,side='left')
    process = Button(frame_main,text='RUN_BENCHMARK',command=rproc,activeforeground='blue',activebackground='white')
    process.pack(fill=Y,side='right')
    mainloop()

    time.sleep(5)
