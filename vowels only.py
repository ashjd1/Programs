a=input()
b="aeiouAEIOU"
f=0
for i in a:
    if i in b:
        f=1
    else:
        f=0
        print("Wrong")
        break
if f==1:
    print("good")
