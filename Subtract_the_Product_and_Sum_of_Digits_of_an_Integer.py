n=int(input())
s=0
m=1
for i in range(n):
    if n>0:
        x=n%10
        s=s+x
        m=m*x
        n=n//10
print(m-s)