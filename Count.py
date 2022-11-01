n=int(input())
x=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if x[i]%2==0:
        c+=1
    else:
        d+=1
print(c,d)