s=input("Enter a string")
c,v=0,0
for i in s:
	if i in "aeiouAEIOU":
		v+=1
	else:
		c+=1
print(v)			
