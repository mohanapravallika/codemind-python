s=input()
c=0
for i in range(0,len(s)):
    if s[i].isupper():
        c=c+1
print(c)