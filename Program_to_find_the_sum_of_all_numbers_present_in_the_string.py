s=input()
c=0
for i in s:
    if i.isnumeric():
        c=c+int(i)
print(c)