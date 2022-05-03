def user_input():
    a,b=int(input("enter value: ")) , int(input("enter value: ") )    #two inputs in one line
    #b=input("enter value: ")
    return(a,b)

def add(a,b):
    return(a+b)

a,b=user_input()
#add(a,b)
print (a,"+",b,"=",add(a,b))
