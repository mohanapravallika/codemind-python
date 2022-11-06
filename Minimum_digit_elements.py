c=int(input())
b=list(map(int,input().split()))
m=max(b)
n=0
for i in b:
    if(len(str(i)))<m:
        m=len(str(i))
for i in b:
    if(len(str(i)))==m:
        n+=1
print(n)