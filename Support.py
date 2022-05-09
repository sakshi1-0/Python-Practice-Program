class student():
	institution = "IIPS"

	def __init__(self,a,b):
		self.a = a
		self.b = b 

	def show(self):
		print("--------------------------")
		print("Marks in Python = ",self.a)
		print("Marks in Python Lab = ",self.b)
		print("--------------------------")

	@classmethod
	def info(self):
		print("Class belongs to ",self.institution)

	@staticmethod
	def about():
		print("This class hold the data of marks obtained by student in python and it's lab in IIPS")

s1 = student(12,10)
s2 = student(13,11)
s3 = student(14,9)
s1.show()
s2.show()
s3.show()
student.info()
student.about()
