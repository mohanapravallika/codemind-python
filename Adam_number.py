n=int(input())#12
k=0
b=n**2#144
k1=0
while n!=0:
    d=n//10
    s=n%10#1 2
    k=k*10+s#21
    n=d
    a=k**2#441
while a!=0:
    d1=a//10
    s1=a%10
    k1=k1*10+s1#144
    a=d1
if(b==k1):
    print("True")
else:
    print("False")