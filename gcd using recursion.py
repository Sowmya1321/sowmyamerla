def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
output = gcd(a,b)
print("Gcd is: ")
print(output)			
