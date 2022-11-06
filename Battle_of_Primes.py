def ispri(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
c=n+m+1
while(True):
    if ispri(c):
        break
    c+=1
print(c-n-m)