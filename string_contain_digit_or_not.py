n=input()
c=0
for j in n:
    if j.isdigit():
        c=c+1
        
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains "+ str(c) +" digit" )