x=list(map(int,input().split()))
d=list(map(int,input().split()))
for i in d:
    print(int(str(i)[::-1]),end=" ")