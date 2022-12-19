import math
def prime(a):
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
n=int(input())
s=str(n)
c=0
for i in s:
    if prime(int(i))==True:
        c+=1
if c==len(s) and prime(n)==True:
    print("Mega Prime")
else:
    print("Not Mega Prime")