import math
def prime(a):
    if a<2:
        return 0
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
m=int(input())
c=2
for i in range(2,m//2+1):
    if prime(i)==0 and m%i==0:
        c+=1
print(c)
        