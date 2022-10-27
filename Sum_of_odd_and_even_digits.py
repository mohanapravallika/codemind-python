n=int(input())
x=list(map(int,input().split()))
c=[]
d=[]
for i in range(n):
    if i%2==0:
        c.append(x[i])
    else:
        d.append(x[i])
e=sum(c)
f=sum(d)
if (e-f)==0:
    print("YES")
else:
    print("NO")
        