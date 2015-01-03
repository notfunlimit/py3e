#import system modules
import sys
import os

#generate local address
local_addr=os.getcwd()
sys.path.append(local_addr+r'\func')

#import functions
import gnrs

#main
if __name__ == '__main__':
	#auto_select takes
	tks=gnrs.frequency(1000000)
	if tks in range(0,10):
		gnrs.make_csv(50)
	elif tks in(10,20):
		gnrs.make_csv(100)
	elif tks in range(20,30):
		gnrs.make_csv(200)
	elif tks in range(30,40):
		gnrs.make_csv(400)
	elif tks >= 40:
		gnrs.make_csv(500)
