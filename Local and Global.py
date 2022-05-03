#local and global declaration
count=1
def plus():
    global count
    count+=1

def minus():
    global count
    count-=1

print("count=",count)
plus()
plus()
minus()
minus()
print("count=",count)
