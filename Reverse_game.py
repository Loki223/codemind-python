def rev(a):
    re=0
    le=len(str(a))-1
    while a>0:
        r=a%10
        re=re+(r*(10**le))
        a=a//10
        le=le-1
    return re
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    print(rev(i),end=" ")
    