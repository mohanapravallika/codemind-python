def len(n):
    l=0
    while(n>0):
        l=l+1
        n=n//10
    return l
def adn(n,x):
    i=0
    m=1
    while(i<x):
        m*=10
        i+=1
    last=n%m
    l=len(n)
    while(l!=x):
        n//=10
        l-=1
    first=n
    return abs(first-last)
n,x=map(int,input().split())
print(adn(n,x))