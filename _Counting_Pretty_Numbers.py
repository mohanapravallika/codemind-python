n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        if j%10==2 or j%10==3 or j%10==9:
            c=c+1
    print(c)