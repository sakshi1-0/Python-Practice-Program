class A:
    def area(self,r=None,l=None):
        
        if(r !=None and l==None ):
            ar=22/7*r*r
            return ar
        elif(r !=None and l !=None ):
            ar=r*l
            return ar
        else:
            print("No provide values")
       

a1=A()
area1=a1.area(3,4)
print(" Area of rectangle",area1)
area2=a1.area(2)
print("Area of circle",area2)
area3=a1.area()


#print("none",area3)
            
