n=int(input())
x=list(map(int,input().split()))
print(abs(sum(x[:len(x)//2])-sum(x[len(x)//2:])))