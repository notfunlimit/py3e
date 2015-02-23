#穷举质数
#coding=utf-8
'''
Created on 2013-7-23
Function: 0--100之间所有素数
@author: BeginMan
To me: be a great man.
-----------------------------------------------------------
'''
from math import sqrt	#从math库引入sqrt函数
result1 = []	#初始化result1列表

for num in range(2,100):	#循环开始
	f = True 	#定义f变量为布尔类型中的true
	for sn in range(2,int(sqrt(num))+1):				#循环sn是否在2到 sqrt(num)的整数部分+1
		if num % sn == 0:				 #如果求余(num/sn)=0的话
			f = False					#f的值为false
		break	#终止循环
	if f:
		result1.append(num)	 #result1列表加入num

print(result1)

