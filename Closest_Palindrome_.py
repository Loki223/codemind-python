def pall(n):
    n=str(n)
    if n==n[-1:-len(n)-1:-1]:
        return 1
    else:
        return 0
n=int(input())
n1=n-1
n2=n+1
c=0
a=[]
while True:
    if pall(n1)==1:
        p1=n1
        a.append(p1)
        c=2
    if pall(n2)==1:
        p2=n2
        a.append(p2)
        c=1
    if c==1 or c==2:
        break
    n1-=1
    n2+=1
print(*a)