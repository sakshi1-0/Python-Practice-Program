#permutation
import fact_fun
print("program to find permutation")

x=int(input("Enter total items: "))
y=int(input("Enter number of item to be arranged: "))
fx=fact_fun.fact(x)
fy=fact_fun.fact(x-y)
p=fx/fy
print("permutation= ",p)
