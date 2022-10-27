i=input()
v="aeiouAEIOU"
c=0
for j in i:
    if j in v:
        c=c+1
if c>0:
    print(c)
else:
    print(0)
    
