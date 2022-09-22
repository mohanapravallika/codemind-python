n=int(input())
l=list(map(int,input().split()))
i=0
k=1
j=2
c=0
while j<n:
    if l[i]%2!=0 and l[k]%2!=0 and l[j]%2!=0:
        c+=1
    i+=1
    j+=1
    k+=1
print(c)