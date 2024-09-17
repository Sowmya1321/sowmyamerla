def fib(n):
	if n<=1:
		return n
	else:
		return (fib(n-1)+fib(n-2))
a=int(input("no of terms"))
if a<=0:
	print("enter a positive integer")
else:
	print("fibanocci sequence")
for i in range(a):
	print(fib(i))					
