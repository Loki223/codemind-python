m,n=map(int,input().split())
l=[]
r=rowsum=0
c=colsum=0
for i in range(m):
    a=list(map(int,input().split()))
    l.append(a)
    for i in a:
        r+=i
    if r>rowsum:
        rowsum=r
    r=0
for i in range(n):
    for j in range(m):
        c+=l[j][i]
    if c>colsum:
        colsum=c
    c=0
if rowsum>colsum:
    print(rowsum)
else:
    print(colsum)