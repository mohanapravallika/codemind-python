n=int(input())
for i in range(n):
    m=input()
    for j in m:
        if j.isdigit():
            print("Yes")
            break
    else:
        print("No")
        