print(" Program to print the fibonacci series..")
n=int(input("How many terms want to print: "))
a=0
b=1
fibo=1
print("Fibonacci series-")
print(a)
while(b<n-1):    
    fibo=a+b
    a=b
    b=fibo
    print(a)
    
