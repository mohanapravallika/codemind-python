x=list(input().split())
v=x[::-1]
g=[]
for i in v:
    v=i[::-1]
    g.append(v)
print(*g)