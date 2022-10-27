n=int(input())
x=list(map(int,input().split()))
d=[]
for i in x:
    if x.count(i)==1:
        d.append(i)
if len(d)!=0:
    print(max(d))
else:
    print(-1)