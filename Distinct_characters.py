n=input()
n=n.lower()
n=n.replace(' ','')
c=[]
for i in n:
    if i not in c:
        c.append(i)
c=sorted(c)
c=''.join(c)
print(c)