import math
def prime(a):
    if a<2:
        return 0
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
def pal(a):
    a=str(a)
    if a==a[-1:-len(a)-1:-1]:
        return 1
m=int(input())
n=m+1
while True:
    if prime(n)==1 and pal(n)==1:
        print(n)
        break
    n+=1
    