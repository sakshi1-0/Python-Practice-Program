def fact(x):
	fact = 1 
	if x == 1 or x == 0 : 
		return 1
	else : 
		for i in range(1,x+1):
			fact = fact*i
		return fact

f = open("sample.txt","w")
for i in range(5,21):
	#f.write("+++++++++++++")
	y = fact(i)
	print(i,y)
	z = "Factorial of "+str(i)+" is "+str(y)
	f.write(z)
	f.write("\n")
	#f.write("+++++++++++++")
f.close()

f = open("sample.txt","r")
data1 = f.read()
print("this is read operation")
print(data1)
dataline = data1.split("\n")
print(dataline)
dataline.pop()
print(dataline)
f.close()