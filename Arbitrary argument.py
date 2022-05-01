def avg(*value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
y=avg(3,4,5)
print(y)
r=avg(2,5,6,1,3)
print(r)
