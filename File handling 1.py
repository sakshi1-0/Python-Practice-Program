f=open("myfirstfile.txt","w")
x=" Movie RRR"
y="Movie KGF"
f.write(x)
f.write("\n")
f.write(y)
f.close()

f=open("myfirstfile.txt","r")
y=f.read()
print(y)
f.close()
