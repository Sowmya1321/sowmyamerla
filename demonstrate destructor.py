class cons:
	def __init__(self):
		self.greet="good morning"
	def display(self):
		print("msg=",self.greet)
	def __del__(self):
		print("object is destroyed")
obj=cons()
obj.display()
print(obj)
del object			







OUTPUT:
msg= good morning
<__main__.cons object at 0x7616c8663dc0>
Traceback (most recent call last):
  File "/home/vitcse/di/sum.py", line 11, in <module>
    del object			
NameError: name 'object' is not defined
object is destroyed
