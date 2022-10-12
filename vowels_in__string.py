n=input()
l=len(n)
v=['a','e','i','o','u','A','E','I','O','U']
a=[]
for i in range(l):
    if n[i] in v:
        if n[i] not in a:
            a.append(n[i])
if a==[]:
    print(-1)
else:
    print(*a)