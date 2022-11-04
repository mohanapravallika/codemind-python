x=int(input())
m=list(map(int,input().split()))
mc=0
index=-1
for i in range(x):
    c=0
    for j in range(x):
        if m[i]==m[j]:
            c+=1
    if(c>mc):
        mc=c
        index=i
if(mc>x//2):
    print(m[index])