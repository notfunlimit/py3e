#add program's address to sys.path

#import system modules
import sys
import os

#define add_sys()
def add_sys():
	local_addr=os.getcwd()
	sys.path.append(local_addr+r'\func')
	sys.path.append(local_addr+r'\deb_')
	sys.path.append(local_addr+r'\libs')
	return 'added'
