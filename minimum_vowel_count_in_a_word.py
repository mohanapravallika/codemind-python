s=input()
s=s.split()
v='aeiouAEIOU'
d=[]
for i in s:
    c=0
    for j in i:
        if j in v:
            c+=1
    d.append(c)
print(min(d))