class employee():
	def __init__(self):
		self.firstname = input("Enter Your First Name : ")
		self.lastname = input("Enter Your Last Name : ")
		self.education = input("Enter Your Educational Qualification : ")
		self.contact_no = input("Enter Your Contact Number : ")
		self.mail_id = input("Enter Your Email Id : ")
		self.address = input("Enter Your address: ")
		self.account_id = input("Enter Your Bank Account Number : ")
		self.adhar_id = input("Enter Your Adhar Card Number : ")

	def show(self) :
		print("=========================================")
		print("Enter Your First Name : ",self.firstname)
		print("Enter Your Last Name : " ,self.lastname)
		print("Enter Your Educational Qualification : ",self.education)
		print("Enter Your Contact Number : ",self.contact_no)
		print("Enter Your Email Id : ",self.mail_id)
		print("Enter Your Address: ",self.address)
		print("Enter Your Bank Account Number : ",self.account_id)
		print("Enter Your Adhar Card Number : ",self.adhar_id)
		print("=========================================")

class office_assistant(employee):
	def __init__(self):
		super().__init__()
		self.salary = input("Enter Your Salary")
		self.grade = input("Enter Your Grade")		


	def show2(self) :
		super().show()
		print("Enter Your Salary : ",self.salary)
		print("Enter Your Grade : ",self.grade)

e1 = office_assistant()
e1.show2()
e1.show()



