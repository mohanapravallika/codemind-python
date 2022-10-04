n=int(input())
rem=0
if n<0:
    n=n*(-1)
    while n>0:
        r=n%10
        k=n//10
        rem=rem*10+r
        n=k
    print(rem*-1)
else:
    while n>0:
        r=n%10
        k=n//10
        rem=rem*10+r
        n=k
    print(rem)