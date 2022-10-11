n=int(input())
x=list(map(int,input().split()))
v=sum(x)
if v%2==0:
    print(1)
else:
    print(0)