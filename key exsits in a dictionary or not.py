def checkKey(dic,key):
	if key in dic.keys():
		print("present, ", end = " ")
		print("value =", dic[key])
	else:
		print("not present")
dic = {'a': 200, 'b': 300, 'c': 400}
key = 'c'
checkKey(dic,key)
key = 'a'
checkKey(dic,key)
