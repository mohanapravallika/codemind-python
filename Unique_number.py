n=int(input())
x=str(n)
a1=[]
a2=[]
for i in x:
    a1.append(i)
    a2.append(i)
z=list(set(a1))
if len(z)==len(a2):
    print("Unique Number")
else:
    print("Not Unique Number")