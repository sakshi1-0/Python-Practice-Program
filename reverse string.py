#string reversal

s=str(input("Enter any string: "))
a=len(s)
reverse=" "
for i in range(a-1,-1,-1):
    reverse+=s[i]
print(reverse)    
    
  
