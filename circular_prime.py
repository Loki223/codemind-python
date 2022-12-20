import math
def prime(a):
    if a<2:
        return 0
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return 0
    return 1
m=int(input())
n=str(m)
if prime(m)==1 and prime(int(n[-1:-len(n)-1:-1])):
    print("circular prime")
elif prime(m)==1 and prime(int(n[-1:-len(n)-1:-1]))!=1:
    print("prime but not a circular prime")
else:
    print("not prime")