from math import sqrt
def prime(a):
    if a<2:
        return False
    for i in range(2,int(sqrt(a))+1):
        if a%i==0:
            return False
    return True
l=[]
n=int(input())
for i in range(2,n+1):
    if n%i==0 and prime(i)==True:
        l.append(i)
b=[2,3,5]
c=0
for i in l:
    if i in b:
        c+=1
if n==1:
    print("Ugly Number")
elif n<=0:
    print("Not Ugly Number")
else:
    if c==len(l):
        print("Ugly Number")
    else:
        print("Not Ugly Number")