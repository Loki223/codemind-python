m,n=map(int,input().split())
r=0
for i in range(m):
    a=list(map(int,input().split()))
    for i in a:
        r+=i
    print(r,end=" ")
    r=0