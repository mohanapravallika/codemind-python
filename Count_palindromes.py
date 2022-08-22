def pal(n):
    x=str(n)
    y=x[::-1]
    if x==y:
        return True
    return False
n=int(input())
x=list(map(int,input().split()))
c=0
for i in x:
    if pal(i):
        c=c+1
print(c)
    