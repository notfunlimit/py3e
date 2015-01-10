import gnrs

def mcsv_run():
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
