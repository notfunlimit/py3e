#Followed GPL v3 License
#github webpage:https://github.com/XDASADX/Pyth0n3c1ipse
#compiler: sublime 2 & Python IDLE

#import system modules
import sys
import os
import time

#generate local address
local_addr=os.getcwd()
sys.path.append(local_addr+r'\func')

#import functions
import gnrs

#main
if __name__ == '__main__':
	#intitialize
	t_avr=gnrs.intitial(10)
	#Automatics
	
	if t_avr in range(0,8):
		gnrs.make_csv(80)
	elif t_avr in(8,20):
		gnrs.make_csv(200)
	elif t_avr in range(20,35):
		gnrs.make_csv(200)
	elif t_avr in range(35,40):
		gnrs.make_csv(400)
	elif t_avr > 40:
		gnrs.make_csv(500)
	else:
		gnrs.make_csv(100)
		
    #halts
	time.sleep(5)
