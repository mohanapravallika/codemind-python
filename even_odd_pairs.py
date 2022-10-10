n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in l:
    if i&1:
        l2.append(i)
    else:
        l1.append(i)
if len(l1)<len(l2):
    for i in range(len(l1)):
        print(l1[i],l2[i],end=" ")
    print(*l2[len(l1):],end=" ")
    if n&1:
        print(0)
elif len(l1)>len(l2):
    for i in range(len(l2)):
        print(l1[i],l2[i],end=" ")
    print(*l1[len(l2):],end=" ")
    if n&1:
        print(0,end=" ")
else:
    for i in range(len(l1)):
        print(l1[i],l2[i],end=" ")