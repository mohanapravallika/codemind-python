s=input()
c=0
for i in range(0,len(s)):
    if s[i].isalpha():
        continue
    elif s[i].isnumeric():
        continue
    elif s[i]==' ':
        continue
    else:
        c=c+1
print(c)