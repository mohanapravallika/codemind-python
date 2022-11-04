n=int(input())
x=list(map(int,input().split()))
c=0
d=0
e=0
f=0
for i in range(n):
    if(x[i]%4)==0:
        c+=1
    elif(x[i]%4)==1:
        d+=1
    elif(x[i]%4)==2:
        e+=1
    elif(x[i]%4)==3:
        f+=1
if(c%2==0 and d%2==0 and e%2==0 and f%2==0):
    print("X")
else:
    print("Y")