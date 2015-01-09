#time counter
import time


def count_used(func):
	t_I=time.clock()
	func
	t_II=time.clock()
	print('used '+str(t_II-t_I))
