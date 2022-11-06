n=int(input())
c=0
for i in range(n):
    for j in range(n):
        if j==c:
            print('0',end="")
        else:
            print('x',end="")
    c+=1
    print()