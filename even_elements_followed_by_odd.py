n=int(input())
l=list(map(int,input().split()))
c=[]
k=[]
for i in range(n):
    if l[i]%2==0:
        c.append(l[i])
    else:
        k.append(l[i])
for j in k:
    c.append(j)
print(*c)
    