
    
priority={"+":1,"-":1,"/":2,"*":2,"^":3}
#convert infix to postfix function
def convert(exp):
    global top
    postfix=[]
    for i in exp:
        if(i.isdigit()):
            postfix.append(i)
        elif(i=="("):
            stk.append(i)
            top=top+1
            
        elif(i==")"):
            while(stk[top]!="("):
                postfix.append(stk.pop())
                top=top-1
            stk.pop()
            top=top-1
        else:
            if(top==-1):
                stk.append(i)
                top=top+1
            elif(stk[top]=='('):
                stk.append(i)
                top=top+1
            elif(priority.get(stk[top])>=priority.get(i)):
                postfix.append(stk.pop())
                top=top-1
                if(top>=0):
                    while(priority.get(stk[top]) == priority.get(i)):
                        postfix.append(stk.pop())
                        top=top-1
                        if(top<0):
                            break
                stk.append(i)
                top=top+1
            elif(priority.get(stk[top])<priority.get(i)):
                stk.append(i)
                top=top+1
                             
    while(top!=-1):
        postfix.append(stk.pop())
        top=top-1
    
    return postfix

#main          
operator = ["+","-","/","*","%"]
numeral = ["0","1","2","3","4","5","6","7","8","9","."]
expression = []
input_exp = input("Enter the expression : ")
print("Input = " , input_exp)
operand = ""
for i in input_exp :
    if i in numeral :
        operand = operand+i
    elif i in operator :
        expression.append(operand)
        expression.append(i)
        operand = ""
    else :
        print("Invalid Character")
        break
expression.append(operand)
print("Input (in list) = ", expression)

stk=[]
top=-1
postfix=convert(expression)
print("Postfix expression: ",postfix)


    
    
