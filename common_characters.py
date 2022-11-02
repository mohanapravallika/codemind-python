s=input()
t=input()
s=s.lower()
t=t.lower()
s=s.replace(" ","")
t=t.replace(" ","")
s=set(s)
t=set(t)
c=""
for i in s:
    if i in t:
        c+=i
c=sorted(c)
c="".join(c)
if len(c)==0:
    print(-1)
else:
    print(c)