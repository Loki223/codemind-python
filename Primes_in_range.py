import math
def prime(a):
    if a<2:
        return 0
    x=0
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if prime(i)==1:
        c+=1
print(c)
        