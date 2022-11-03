s=input()
r=input()
s=s.lower()
r=r.lower()
s=s.replace(' ','')
r=r.replace(' ','')
c=[]
for i in r:
    if i not in s:
        c.append(i)
for i in s:
    if i not in r:
        c.append(i)
f=[]
for i in c:
    if i not in f:
        f.append(i)
f=sorted(f)
f=''.join(f)
print(f)
        
