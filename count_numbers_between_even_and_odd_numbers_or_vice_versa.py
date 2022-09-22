def slide(n,l,i,c):#7 l 0-6 0
    if i>=n-2:
        return c
    if l[i]%2==0 and l[i+2]%2!=0:
        return slide(n,l,i+1,c+1)
    elif l[i]%2!=0 and l[i+2]%2==0:
        return slide(n,l,i+1,c+1)
    return slide(n,l,i+1,c)
n=int(input())#7
l=list(map(int,input().split()))#1 2 4 5 6 7 7
i=0
c=0
print(slide(n,l,i,c))