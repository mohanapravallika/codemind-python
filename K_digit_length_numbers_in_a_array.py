n,m=map(int,input().split())
x=list(map(int,input().split()))
f=0
for i in x:
    k=abs(i)
    b=str(k)
    c=len(b)
    if c==n or c==m:
        f=f+1
print(f)
