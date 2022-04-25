#number maximum in three numbers

a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))

if(a==b and b==c and c==a):
    print("All values are same")

elif(a==b and c<a):
    print(a,"and" ,b,"are same and greater than",c)

elif(a==c and b<a):
    print(a,"and" ,c,"are same and greater than",b)

elif(c==b and a<b):
    print(c,"and" ,b,"are same and greater than",a)

elif(a==b and c>a):
    print(a,"and" ,b,"are same and smaller than",c)

elif(a==c and b>a):
    print(a,"and" ,c,"are same and smaller than",b)

elif(c==b and a>b):
    print(c,"and" ,b,"are same and smaller than",a)    
    
elif(a>b and a>c):
    print(a,'is greater than', b,'and', c)

elif(b>c and b>a):
    print(b,' is greater than ',a, 'and' ,c)
    
else:
    print(c,' is greater than', a, 'and ',b)
