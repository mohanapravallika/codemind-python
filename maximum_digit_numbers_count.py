n=input()
m=list(map(str,input().split()))
x=[]
y=[]
for i in m:
    c=len(i)
    x.append(c)
z=max(x)
for j in m:
    if z==len(j):
        y.append(j)
print(*y)