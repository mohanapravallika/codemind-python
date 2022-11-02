s=input()
s=s.split()
c=[]
d=[]
for i in s:
    c.append(min(i))
    c.append(max(i))
print(*c)