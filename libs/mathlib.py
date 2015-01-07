#mathlib
from math import sqrt

class algebra:
	#absolute value;|x|
	def abs(x):
		if x<=0:
			x=-x
		else:
			x=x
		return x

	#factorial ;x is an integer;x!
	def fac(x):
		if int(x)>=1:
			n=1
			for i in range(1,int(x)+1):
				n*=i
			return n
		else:
			return('Invaild Number')

class analytic_geometry:
	#fomula of distance between two points
	#pint_I is a list of a point such as[x1,y1] ,pint_II is a list of[x2,y2]
	#√((x2-x1)^2+(y2-y1)^2))
	def dis_t_points(pint_I,pint_II):
		return sqrt(((pint_II[0]-pint_I[0])**2)+((pint_II[1]-pint_I[1])**2))
    
    #fomula of distance between point to line
    #pint is a list of a point such as[x,y],line is a list of a line such as[a,b,c](ax+by+c=0)
    #abs(a*x1+b*y1+c)/sqrt(a^2+b^2)
	def dis_line_point(pint,line):
		return abs(line[0]*pint[0]+line[1]*pint[1]+line[2])/sqrt(line[0]**2+line[1]**2)
