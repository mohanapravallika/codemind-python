s=input()
t=input()
s=s.lower()
t=t.lower()
a=s.split()
b=t.split()
c=0
for i in b:
    if i in a:
        c+=1
print(c)