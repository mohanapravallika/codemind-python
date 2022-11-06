n=int(input())
x=list(map(int,input().split()))
s=''
for i in x:
    s+=str(i)
print(int(s,2))