l = []
n=int(input("enter the number of elements in the list:"))
for i in range(n):
	 ele = int(input("enter the element"))
	 l.append(ele)
print("list = ",l)
print("Maximum Element = ",max(l))
print("Minimum Element = ",min(l))
print("The position of maximum element",l.index(max(l)))
print("The position of minimum element",l.index(min(l)))	
