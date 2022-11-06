s=input()
s=s.replace(" ","")
k=sorted(list(s))
print(k[0],s.count(k[0]),k[len(k)-1],s.count(k[len(k)-1]))