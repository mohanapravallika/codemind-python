n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if x.count(i)>1:
        print(i)
        break