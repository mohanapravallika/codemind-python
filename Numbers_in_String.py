s=input()
n=0
for x in s:
    if x.isdigit():
        z=int(x)
        n=n+z
print(n)