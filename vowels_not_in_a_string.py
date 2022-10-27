i=input()
v="aeiou"
a=[]
b=[]
for j in i:
    if j in v:
        if j not in a:
            a.append(j)
for j in v:
    if j not in a:
        b.append(j)
if len(b)>0:
    print(*b)
else:
    print(0)