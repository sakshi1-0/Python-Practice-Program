#calculator
print("                                                !!Welcome to sakshi's calculator!!")
#for addition calculation
def addition(a1,a2):
    add=a1+a2
    return(add)

#for multiplication calculation
def multiply(m1,m2):
    mul=m1*m2
    return(mul)

#for division calculation
def division(d1,d2):
    div=d1/d2
    return(div)

#for subtraction calculation
def subtract(s1,s2):
    sub=s1-s2
    return(sub)

#for modulus calculation
def modulus(l1,l2):
    mod=l1%l2
    return(mod)

#for  findingsquare
def sqr(q1):
    sq=q1*q1
    return(sq)

#for finding power
def power(c1,c2):
    pw=c1**c2
    return(pw)

#for cube
def cube(cb):
    ce=cb**cb
    return(ce)

#for square root
def sqroot(sr):
    rt=sr**0.5
    return(rt)

#for cube root
def  curoot(cr):
    ct=cr**(1/3)
    return(ct)
    
  
 

#start
def cal():
    print("What opeararion  want to perform 3 for binary or 4 for unary operation? ")                 #binary or unary
    bn=str.lower(input("Enter your choice: "))
    print("What type of value you want to enter 1 for integer or 2 for float :-  ")                             #int or float
    i=str.lower(input("Enter your choice: "))
    if(i=='integer' and bn=='binary'):                                                                                                           #if user choose int
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        print("You entered",a,"and",b)
    elif(i=='float' and bn=='binary'):                                                                                                      #if user choose float
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))
        print("You entered",a,"and",b)        
    elif(i=='interger' and bn=='unary'):
         a=int(input("Enter first number: "))
         print("You entered",a)
    elif(i=='float' and bn=='unary'):
         a=float(input("Enter first number: "))
         print("You entered",a)
    else:
        print("Invalid number please enter valid number!!")
        exit()
    #arithmetic operation choices
    if(bn=="binary"):   
        print("select 1 for addition")
        print("select 2 for subtraction")
        print("select 3 for multiplication")
        print("select 4 for division")
        print("select 5 for modulus")
        print("select 6 for power")
        
    else:
        print("select 7 for square")
        print("select 8 for cube")
        print("select 9 for square root")
        print("select 10 for cube root")
    user=int(input("what operation want to perform:"))
    if(user==1):
        x=addition(a,b)
        print(a,"+",b,"=",x)
    elif(user==2):
        y=subtract(a,b)
        print(a,"-",b,"=",y)
    elif(user==3):
        z=multiply(a,b)
        print(a,"*",b,"=",z)
    elif(user==4):
        if(b==0):
            print("Error!!can't divide by zero")
        else:   
            u=division(a,b)
            print(a,"/",b,"=",u)
    elif(user==5):
        if(b==0):
            print("Error!!can't divide by zero")
        else:   
            v=modulus(a,b)
            print(a,"%",b,"=",v)
    elif(user==6):
        o=power(a,b)
        print("power",a,"=",o)
    elif(user==7):
        w=sqr(a)
        print("square of",a,"=",w)
    elif(user==7):
        o=power(a,b)
        print("power",a,"=",o)
    elif(user==8):
        p=cube(a)
        print("cube of",a,"=",p)
    elif(user==9):
        s=sqroot(a)
        print("square root of",a,"=",s)
    elif(user==10):
        q=curoot(a)
        print("cube root of",a,"=",q)
        
    else:
         print("invalid number,please enter valid number!!")

cal()
#ask user to calculate again
ch=str.lower(input("You want to play again y for yes n for no: "))
if(ch=="y"):
    cal()
else:
    print("THANK YOU!!")
exit()
