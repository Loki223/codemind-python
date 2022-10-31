m,n=map(int,input().split())
l=[]
c=colsum=0
for i in range(m):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(n):
    for j in range(m):
        c+=l[j][i]
    if c>colsum:
        colsum=c
    c=0
print(colsum)