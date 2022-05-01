print(" Program to print the factorial of user defined number")


def fact(x):
    y=1
    if(x==1 or x==0):
        return y
    else:
        y=x*fact(x-1)
        return y

val=int(input("Enter number to find its factorial: "))   
funct_val=fact(val)
print("Factorial of {} is {}".format(val,funct_val))
    
