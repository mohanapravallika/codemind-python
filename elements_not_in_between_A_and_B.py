n=int(input())
x=list(map(int,input().split()))
n,m=map(int,input().split())
l=[]
for i in x:
    if i<n or i>m:
        l.append(i)
if len(l)!=0:
    print(*l)
else:
    print(-1)