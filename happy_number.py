def hpy(n):
    x=n
    s=0
    while x>0:
        c=x%10
        s=(s+(c*c))
        x=x//10
    return s
n=int(input())
hpy(n)
s=n
while s>9:
    s=hpy(s)
if s==1 or s==7:
    print("True")
else:
    print("False")