#permutation
print("program to find permutation")
def fact(n):    
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
    return(fact_n)

x=int(input("Enter total: "))
y=int(input("Enter value: "))
fx=fact(x)
fy=fact(x-y)
p=fx/fy
print("permutation= ",p)
