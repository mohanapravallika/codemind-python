s=input()
c=input()
d=0
for i in s:
    if i==c:
        d+=1
if d!=0:
    print(d)
else:
    print(-1)