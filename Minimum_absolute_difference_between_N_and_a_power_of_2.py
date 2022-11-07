import math
n=int(input())
x=int(math.log(n,2))
a=2**x
b=2**(x+1)
print(min(abs(a-n),abs(b-n)))