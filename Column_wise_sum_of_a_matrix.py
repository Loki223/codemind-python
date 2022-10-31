m,n=map(int,input().split())
l=[]
c=0
for i in range(m):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(n):
    c=0
    for j in range(m):
        c+=l[j][i]
    print(c,end=" ")