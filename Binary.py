a=int(input("Enter your number :- "))
li=[]
while(True):
    b=a%2
    li.append(str(b))
    a=a//2
    if(a==0):
        break
print(("".join(li))[::-1])
