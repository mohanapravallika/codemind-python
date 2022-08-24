x=list(input().split(" "))
k=""
for i in range(len(x)):
    if i%2==0:
        k=k+" "+x[i][::-1]
    else:
        k=k+" "+x[i]
m=k[1:]
print(m)
    
