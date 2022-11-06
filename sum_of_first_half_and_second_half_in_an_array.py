n=int(input())
x=list(map(int,input().split()))
print(sum(x[:len(x)//2]))
print(sum(x[len(x)//2:]))