s=input()
s=s.split()
l=[]
c=0
v="aeiouAEIOU"
for i in s:
    c1=0
    for j in i:
        if j in v:
            c1+=1
    l.append(c1)
for i in l:
    if i==min(l):
        c+=1
print(c)
    