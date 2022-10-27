s=input()
s=s.split()
c=c1=0
for i in s:
    c+=ord(max(i))
    c1+=ord(min(i))
print((c-c1))