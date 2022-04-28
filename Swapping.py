#swap with 3 variable

print("This script  is intended to swap the values of two data variable using a third temporary variable")

a=(input("Enter first  number: "))
b=(input("Enter second number: "))

print (" Value Before swapping ")
print ("a="+a)
print("b="+b)

a=int(a)
b=int(b)
#a,b=b,a
a=a+b
b=a-b
a=a-b
#temp=a
#a=b
#b=temp

print(" Values After swapping ")
print("a=" +str(a))
print("b=" +str(b))


