#import system modules
import sys
import os

#generate local address
local_addr=os.getcwd()
sys.path.append(local_addr+r'\func')

#import functions
import gene_result


if __name__ == '__main__':
	gene_result.make_csv(1000)
