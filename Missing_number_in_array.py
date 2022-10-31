n=int(input())
for i in range(n):
    k=int(input())
    m=list(map(int,input().split()))
    for j in range(1,k+1):
        if j not in m:
            print(j)
        