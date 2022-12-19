import math
def prime(a):
    if a<2:
        return "not a prime"
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            return "not a prime"
    return "prime"
n=int(input())
print(prime(n))