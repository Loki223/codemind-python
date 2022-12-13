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
m=l.index(min(l))
n=l.index(max(l))
if m>n:
    l1=[l[i] for i in range(len(l)) if i>=n and i<=m]
else:
    l1=[l[i] for i in range(len(l)) if i>=m and i<=n]
for i in l1:
    if prime(i)==True:
        c+=1
print(c)