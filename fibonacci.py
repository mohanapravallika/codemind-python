def fib(n):
    a=0
    b=1
    c=3
    print(a,b,end=" ")
    while c<n:
        s=a+b
        a=b
        b=s
        c=c+1
        print(b,end=" ")
    print(a+b)
fib(int(input()))