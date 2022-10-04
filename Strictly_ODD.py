def so(n,x):
    for i in range(n):
        if x[i]%2!=0:
            if i%2==0:
                return False
    return True
n=int(input())
x=list(map(int,input().split()))
print(so(n,x))