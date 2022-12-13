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
s=0
c=0
for i in l:
    if prime(i)==True:
        s+=i
        c+=1
avg=s/c
print("{:.2f}".format(avg))