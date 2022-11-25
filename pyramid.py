a=5
for i in range(a):
    for j in range(a-i-1):
        print(" ",end="")
    for i in range(i+1):
        print("*",end=" ")
    print()
    
