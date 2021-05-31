# -*- coding: utf-8 -*
import time

# O(n ** 2)
def O(n):
	start_time = time.perf_counter()
	a = 5 # 1
	b = 6 # 1
	c = 10 # 1
	for i in range(n): # n * n
		for j in range (n):
			x = i * i
			y = j * j
			z = i * j
		for k in range(n):
			w = a * k + 45
			v = b * b
	d = 33 # 1
	end_time = time.perf_counter()
	counter_time = end_time-start_time
	print("程序运行%s次时间%sS" % (n, counter_time))

O(10)
O(100)
O(1000)

