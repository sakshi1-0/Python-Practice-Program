#importing methods

#first method
import math                                                        #with keyword import
x=4
y= math.sqrt(x)
print(x," " ,y)

#second method                                             #make it alias
import math as m
x=4
y= m.sqrt(x)
print(x," " ,y)

#third method                                                  #takes selective function
from math import sqrt
x=4
y= sqrt(x)
print(x," " ,y)

#third method
from math import *                                         #all funtion will import
x=4
y= sqrt(x)
print(x," " ,y)
