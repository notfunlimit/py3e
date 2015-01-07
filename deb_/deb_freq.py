#I.S.M.
import sys
import os

#define new address
func=['f','u','n','c']

#A.S.L.A.
local_addr=list(os.getcwd())
local_addr=''.join(local_addr[:-4]+func)
sys.path.append(local_addr)

#I.L.F.
import gnrs

#D.C.
if __name__ == '__main__':
	gnrs.deb_inst_freq(20)
	os.system('cls')
