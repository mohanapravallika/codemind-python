i=input()
v="aeiou"
v1="AEIOU"
a=[]
b=[]
for j in i:
    if j in v:
        if j not in a:
            a.append(j)
    if j in v1:
        if j not in a:
            b.append(j)
if len(a)==5 or len(b)==5:
    print("True")
else:
    print("False")