n=int(input())
x=n**2
c=0
while x>0:
    m=x%10
    c=c+m
    x=x//10
if c==n:
    print("Neon Number")
else:
    print("Not Neon Number")