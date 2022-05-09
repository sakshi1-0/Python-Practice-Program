class school():
	"""docstring for ClassName"""
	def __init__(self):
		self.name = input("Enter School name : ")
		self.address = input("Enter School address : ")

	def show(self):
		print("{} is situated at {}".format(self.name,self.address))

item1 = school()
item1.show()



		
	