s=input()
s=s.lower()
s=s.replace(' ','')
c=0
for i in s:
    if s.count(i)==1:
        c=c+1
print(c)