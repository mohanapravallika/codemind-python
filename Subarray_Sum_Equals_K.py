a=list(map(int,input().split()))
x=list(map(int,input().split()))
f=0
for i in range(len(x)):
    c=0
    for j in range(i,len(x)):
        c+=x[j]
        if c==a[1]:
            f+=1
print(f)
        