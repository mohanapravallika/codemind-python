def fun(a):
    b=0
    while True:
        c=a%10
        a=a//10
        b=b+c
        if a==0:
            if b<10:
                return b
            else:
                a,b=b,0
    return b
n=int(input())
b=fun(n)
print(b)