s=input()
x=s.split()
c=x[-1]
d=[]
for char in c:
    if char not in d:
        d.append(char)
print(d[0])
    