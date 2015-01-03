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
	if tks in range(0,8):
		gnrs.make_csv(80)
	elif tks in(8,20):
		gnrs.make_csv(200)
	elif tks in range(20,35):
		gnrs.make_csv(200)
	elif tks in range(35,40):
		gnrs.make_csv(400)
	elif tks > 40:
		gnrs.make_csv(500)
	else:
		print('Error:please restart')
