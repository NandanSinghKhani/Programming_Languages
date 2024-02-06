def fib(m):
	if m==0:
		return 0
	elif m==1:
		return 1
	else:
		return fib(m-1)+fib(m-2)
print(fib(12))
	