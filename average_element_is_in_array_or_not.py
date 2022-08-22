n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    if l[i]:
        s=s+l[i]
        r=s//n
if r in l:
    print("True")
else:
    print("False")
    
        
        
    