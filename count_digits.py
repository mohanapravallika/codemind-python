n=int(input())
x=list(map(int,input().split()))
for i in x:
    print(len(str(abs(i))),end=" ")