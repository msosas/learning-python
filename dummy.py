def fib():
	a = 0
	b = 1
	c = 0
	while True:
		yield a
		
		a = b
		b = b + c
		c = a
		if a > 100:
			raise StopIteration


for x in fib():
 	print(x)
