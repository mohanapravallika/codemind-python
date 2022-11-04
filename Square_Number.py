n=int(input())
c=0
for i in range(0,n):
    for j in range(i+1,n+1):
        if(i*i+j*j)==n:
            c=1
if c==0:
    print("False")
elif c==1:
    print("True")