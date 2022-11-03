s=int(input())
x=list(map(int,input().split()))
c=[]
for i in x:
    if x.count(i)==1:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)