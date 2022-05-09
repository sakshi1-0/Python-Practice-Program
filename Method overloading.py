#method Overloading 



class student:
        

        def avg(self, *x):
                average = 0
                sum = 0
                if len(x) == 0:                   
                        average = "No Values Provided"
              else:
	   for i in x :
                              sum +=i
	         average = sum/len(x)

             return average



s1 = student()
avg5 = s1.avg(12,112,154,12,452,4,35,2,1,5,5,32,1,3,6,3,1,3,4,5,3,2,3,1)
avg1 = s1.avg(12,13,14)
avg2 = s1.avg(12,13)
avg3 = s1.avg(12)
avg4 = s1.avg()



print(avg5)
print(avg1)
print(avg2)
print(avg3)
print(avg4)
