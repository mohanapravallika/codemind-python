n=int(input())
t=n
s=[]
while t>0:
    r=t%10
    s.append(r)
    t=t//10
print(max(s))
