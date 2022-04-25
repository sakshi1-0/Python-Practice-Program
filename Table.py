#printing table of user defined integer

n=int(input("enter a number to get table = "))
m=n*10
count = 1
for i in range(n,m+1,n):
    #print(n,"*",i//n,"=",i)
    print("{} * {} = {}".format(n,count,i))
    count=count+1
