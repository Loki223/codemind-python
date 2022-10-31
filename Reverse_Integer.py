n=int(input())
v=n
rev=0
if n<0:
    n=n*(-1)
c=len(str(n))-1
while n:
    i=n%10
    rev+=i*(10**c)
    n=n//10
    c=c-1
if v<0:
    print(-rev)
else:
    print(rev)
    