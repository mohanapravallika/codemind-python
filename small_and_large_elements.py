s=input()
s=s.split()
x=[]
c=[]
d=[]
x.append(s[0])
for i in x:
    c.append(min(i))
d.append(s[-1])
for i in d:
    c.append(max(i))
print(*c)
    