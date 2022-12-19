import math
def prime(a):
    if a<2:
        return False
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return False
    return True
n=int(input())
for i in range(n):
    t=int(input())
    t1=t-1
    t2=t+1
    while True:
        if prime(t)==True:
            print(t)
            break
        if prime(t1)==True:
            print(t1)
            break
        if prime(t2)==True:
            print(t2)
            break
        t1-=1
        t2+=1
