import re 
class contact():

	def __init__(self,first,last,phone,email):
		self.first = first
		self.last = last
		self.phone = phone 
		self.email = email

	def add(self):
		f = open("smart.txt","a")
		f.write("{}:{}:{}:{}\n".format(self.first,self.last,self.phone,self.email))
		f.close()

	def show(self):
		print("----------------------------")
		print("First Name : {}".format(self.first))
		print("Last Name : {}".format(self.last))
		print("Contact Number : {}".format(self.phone))
		print("Email : {}".format(self.email))

	def update(self):
		print("----------------------------")
		print("First Name : {}".format(self.first))
		print("Last Name : {}".format(self.last))
		print("Contact Number : {}".format(self.phone))
		print("Email : {}".format(self.email))
		print("----------------------------")

		change =int(input("What you wish to change ? \n 1. First Name \n 2. Last Name \n 3. Phone \n 4. Email \n Enter your choice :  "))
		value1 = input("Enter value to be updated : ")
		if change == 1 :
			self.first = value1
		elif change == 2 :
			self.last = value1
		elif change == 3 :
			self.phone = value1 
		elif change == 4 :
			self.email = value1
		else : 
			print("invalid choice")

	
def getdata():
	f = open("smart.txt","r")
	x = f.read()
	y = x.split("\n")
	y.pop()
	z = []
	for i in y : 
		item = i.split(":")
		z.append(item)
	return z

def search(dataline):
	value = input("Enter Value to be searched : ")
	for i in dataline : 
		if value in i :
			return i
	else : 
		return None

def validate(a,b,c,d):
	name_regex = "[a-zA-Z]"
	email_regex =  "[a-z0-9]+@[a-z0-9]+\.[a-z]"
	phone_regex = "[0-9]"

	if re.search(name_regex,a) and re.search(name_regex,b):
		if re.search(phone_regex,c):
			if re.search(email_regex,d):
				print("All Inputs are valid")
				return True
			else :
				print("Invalid Email")
				return False
		else :
			print("Invalid Phone")
			return False
	else :
		print("Invalid Name")
		return False

print("Welcome to Our Contact Directory")
choice = int(input("Please select a choice \n 1. Show All Contact \n 2. Search Contact \n 3. Add New Contact \n 4. Update Contact \n 5. Delete Contact \n Enter Your Choice :  "))
if choice == 1 : 
	line = getdata()
	for i in line : 
		item = contact(i[0],i[1],i[2],i[3])
		item.show()
	print("----------------------------")

elif choice == 2 :
	dataline = getdata()
	x = search(dataline)
	if x == None :
		print("No Record Found")
	else:
		item = contact(x[0],x[1],x[2],x[3])
		print("Record Found")
		item.show()
		print("----------------------------")


elif choice == 3 :
	first_name = input("First Name : ")
	last_name = input("Last Name : ")
	phone = input("Contact Number : ")
	email = input("Email : ")
	value = validate(first_name,last_name,phone,email)
	if value == True :
		contact1 = contact(first_name,last_name,phone,email)
		contact1.add()
	else : 
		print("Try again")

elif choice == 4 :
	dataline = getdata()
	value = input("Enter Record to be Updated : ")
	for i in dataline :
		if value in i :
			item = contact(i[0],i[1],i[2],i[3])
			item.update()
			dataline.remove(i)
			print(dataline)
			list2 = [item.first,item.last,item.phone,item.email]
			dataline.append(list2)
			print(dataline)
			for j in dataline : 
				item2 = contact(j[0],j[1],j[2],j[3])
				item2.add()
			break
	else : 
		print("No Record Found")

elif choice == 5 :
	remove()
else : 
	print("Invalid Choice")