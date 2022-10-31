m,n=map(int,input().split())
l=[]
r=rowsum=0
for i in range(m):
    a=list(map(int,input().split()))
    l.append(a)
    for i in a:
        r+=i
    if r>rowsum:
        rowsum=r
    r=0
print(rowsum)