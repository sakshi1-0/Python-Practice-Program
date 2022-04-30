print(" Program that asks the user for a number and then prints out a list of all the divisors of that number")
n=int(input("Enter number to find its factors: "))

print("Divisors/Factors of given number-")

i=1
while(i<=n):    
   if(n%i==0):
       print(i)
   i+=1
