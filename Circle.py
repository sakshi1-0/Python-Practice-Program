#area and circumference of circle


print("Program to find area and circumfrence of circle")
def circle(r):
    a=3.14*r*r
    a=round(a,7)
    c=2*3.14*r
    return(a,c)
r=float(input("Enter radius of circle: "))
a,c=circle(r)
print("area of circle= ",a)
print("circumference of circle= ",c)
   


    
