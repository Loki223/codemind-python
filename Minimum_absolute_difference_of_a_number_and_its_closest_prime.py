import math
def prime(a):
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
n=int(input())
t1=n-1
t2=n+1
while True:
    if prime(n)==True:
        p=n
        break
    if prime(t1)==True:
        p=t1
        break
    if prime(t2)==True:
        p=t2
        break
    t1-=1
    t2+=1
print(abs(p-n))