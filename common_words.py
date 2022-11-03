s=input()
r=input()
s=s.lower()
r=r.lower()
a=s.split()
b=r.split()
c=[]
for i in b:
    if i in a:
        c.append(i)
print(*c)