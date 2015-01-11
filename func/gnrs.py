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
import tkinter.font as tkFont
import tkinter.messagebox as tkMessagebox
import webbrowser

local_addr=''.join((list(os.getcwd())[:-4]))
sys.path.append(local_addr)

#import adsys
import run

loc_addr=os.getcwd()
csv_save_addr=loc_addr+r'\result'

#create save directory
def create_dire():
    if os.path.exists(csv_save_addr)==1:
        pass
    else:
        os.mkdir(csv_save_addr)

create_dire

#benchmark part
class benchmark():
#part I
    def frequency(x):      #bigger is better ,unit:MHz
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

        
        #start
        T_A=time.time()
        print('Benchmark started at:'+time.strftime('%Y-%m-%d-%H:%M:%S'))
        info_src.insert(1.0,'Benchmark started at:'+time.strftime('%Y-%m-%d-%H:%M:%S')+'\n')
        file=open(csv_save_addr+'\\result-'+time.strftime('%Y-%m-%d-%H-%M-%S')+'#'+str(int(x))+'.csv','w')
        
        #main
        for ii in range(0,int(x)):
                #console part
                resultx=benchmark.frequency(100000)
                file.write(str(resultx)+'\n')
                print(str(ii)+'/'+str(int(x)))
                total+=resultx

                #GUI Part
                info_src.insert(1.0,str(ii)+'/'+str(int(x))+'\n')
                info_src.update()

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
        info_src.insert(1.0,'Result saved at:'+csv_save_addr+'\n')
        info_src.insert(1.0,'Average:'+str(total/int(x))+'MHz'+'\n')
        info_src.update()
        print('#'*40)
        return total/(int(x))

#part III intitalizing
    def intitial(x):
        print('intitalizing...')
        tks=0
        for i in range(0,x):
            tks+=benchmark.frequency(1000000)
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
class gui_func():
    def wait_n_clear(x,textbox):
        time.sleep(x)
        textbox.delete(0.0, END)

    def a_t_b():
        tkMessagebox.showinfo('About','Pyth0n3c1ipse\n'
                        +'An benchmark program on python platform\n'
                        +'Published on : github.com/xdasadx/pyth0n3c1ipse\n'
                        +'Github ID : XDASADX\n'
                        +'E-mail address : leemailbox1@gmail.com\n'
                        +'\n')

    def rproc():
        run.mcsv_run()
        #wait_n_clear(5,info_src)

    def o_result():
        os.startfile(csv_save_addr)
        #Notes

    def git_addr():
        github_dire=r'https://github.com/XDASADX/Pyth0n3c1ipse'
        webbrowser.open(github_dire)

    def get_src():
        src_addr=r'https://github.com/XDASADX/Pyth0n3c1ipse/archive/X_BENCH_MARK.zip'
        # webbrowser.open(src_addr)

#GUI FRAME
frame_main=Tk()
frame_main.iconbitmap('res/icon/ICO_32x32.ico')
frame_main.title("Pyth0n3c1ipse")
frame_main.geometry('480x76')
frame_main.resizable(False, False)

menubar = Menu(frame_main)
frame_main['menu'] = menubar

benchmenu = Menu(menubar,tearoff = 1)
settingmenu = Menu(menubar,tearoff = 1)
helpmenu = Menu(menubar,tearoff=1)

menubar.add_cascade(label = 'Benchmark',menu = benchmenu)
benchmenu.add_checkbutton(label = 'Start Benchmark',command = gui_func.rproc)
benchmenu.add_checkbutton(label = 'Result',command = gui_func.o_result)
benchmenu.add_separator()
benchmenu.add_checkbutton(label = 'Exit',command = frame_main.quit)

menubar.add_cascade(label = 'Help',menu = helpmenu)
helpmenu.add_checkbutton(label = 'About', command = gui_func.a_t_b)
helpmenu.add_separator()
helpmenu.add_checkbutton(label = 'Github', command = gui_func.git_addr)
helpmenu.add_checkbutton(label = 'Get sourcecode', command = gui_func.get_src)

logo_bar = os.getcwd()+r'\res\items\bar_extrafine.gif'
img = PhotoImage(file=logo_bar)
logo_lbl=Label(frame_main)
logo_lbl.config(image=img)
logo_lbl.pack(side='bottom')


process = Button(frame_main,text='RUN_BENCHMARK',command=gui_func.rproc,activeforeground='navy',activebackground='white')
#button_img=PhotoImage(loc_addr+r'\res\items\run.gif')
#process = Button(frame_main,width=32,height=32,image=button_img,command=gui_func.rproc)
process.pack(side='right')

info_src=Text(frame_main,fg='midnight blue')
info_src.pack(side='left')
info_src.insert(INSERT, "Pyth0n3c1ipse non-finished version")

mainloop()
