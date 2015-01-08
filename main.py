#Followed GPL v3 License
#github webpage:https://github.com/XDASADX/Pyth0n3c1ipse
#compiler: sublime 2 & Python IDLE
#contributor: XDASADX leemailbox1@gmail.com
#            

#import system modules
import sys
import os
import time

#generate local address
loc_addr=os.getcwd()
sys.path.append(loc_addr)
import adsys

adsys.add_sys()

#import functions
import gnrs

#main
if __name__ == '__main__':
	#intitialize
	t_avr=gnrs.intitial(10)
	#Automatics
	
	if t_avr in range(0,8):
		gnrs.make_csv(80)
	elif t_avr in range(8,20):
		gnrs.make_csv(100)
	elif t_avr > 20:
		gnrs.make_csv(200)
	else:
		gnrs.make_csv(100)
		
		
    #halts
	time.sleep(5)
