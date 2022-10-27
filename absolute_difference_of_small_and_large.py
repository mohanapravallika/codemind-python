s=input()
x=s.split()
c=c1=0
d=[]
for i in x:
    c=ord(max(i))
    c1=ord(min(i))
    d.append((c-c1))
print(*d)