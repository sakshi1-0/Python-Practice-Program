#prime number
num=int(input("Enter any number to find itd prime number or not: "))
i=2
while(i<=num-1):
    if(num%i==0):
        print("Given number is not a prime")
        break
    else:
        print("number is prime")
        break
else:
    print("number is not prime")
