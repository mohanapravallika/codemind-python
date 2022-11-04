n=int(input())
x=list(map(int,input().split()))
c=0
for i in set(x):
    c+=x.count(i)//2
print(c)