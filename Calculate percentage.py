# caluclate percantage
a=int(input('Enter marks of Physics'))
b=int(input('Enter marks of Chemistry'))
c=int(input('Enter marks of Maths'))
d=int(input('Enter marks of Hindi'))
e=int(input('Enter marks of English'))
total=a+b+c+d+e
print('Total of your marks=',total)
aver=total/5
print('percentage=',aver)
if(aver==100 and aver<=90):
    print('Grade=A+')
elif(aver>=80 and aver<90):
    print('Grade=A')
elif(aver>=70 and aver<80):
    print('Grade=B+')
elif(aver>=60 and aver<70):
    print('Grade=B')
elif(aver>=50 and aver<60):
    print('Grade=c+')
elif(aver>=40 and aver<50):
    print('Grade=c')
else:
    print('Fail')
