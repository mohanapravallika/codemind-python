n=int(input())
x=list(map(int,input().split()))
b=n//2
n=x[::-1]
for i in range(b):
    print(n[i],end=" ")
for i in range(b):
    print(x[i],end=" ")