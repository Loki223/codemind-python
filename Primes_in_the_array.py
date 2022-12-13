import math
def prime(a):
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if prime(i)==True:
        c+=1
print(c)