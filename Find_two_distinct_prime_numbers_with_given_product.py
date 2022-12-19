import math
def prime(a):
    if a<2:
        return "not a prime"
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return "not a prime"
    return "prime"
n=int(input())
l=[i for i in range(1,n+1) if prime(i)=="prime"]
c=0
for i in l:
    for j in l:
        if i*j==n:
            print(i,j,end=" ")
            c+=1
    if c==1:
        break
if c==0:
    print(-1)