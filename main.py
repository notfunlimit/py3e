#import system modules
import sys
import os

#generate local address
local_addr=os.getcwd()
sys.path.append(local_addr+r'\func')

#import functions
import generesult


if __name__ == '__main__':
	generesult.make_csv(1000)
