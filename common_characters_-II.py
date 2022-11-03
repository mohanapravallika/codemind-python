s=input()
r=input()
s=s.lower()
r=r.lower()
s=s.replace(' ','')
r=r.replace(' ','')
c=[]
for i in r:
    if i in s:
        c.append(i)
for i in s:
    if i in r:
        c.append(i)
f=[]
for i in c:
    if i not in f:
        f.append(i)
print(len(f))