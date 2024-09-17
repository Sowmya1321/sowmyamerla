l = [132,667,641,467,781]
def second_largest(l):
	l.sort()
	return l[-2]
print("the second largest element is: ",second_largest(l))
