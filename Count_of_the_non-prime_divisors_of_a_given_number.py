n=int(input())
c=0
for i in range(1,n+1,1):
    if n%i==0:
        d=0
        for k in range(1,i+1):
            if i%k==0:
                d+=1
        if d>2 or d==1:
            c+=1
print(c)