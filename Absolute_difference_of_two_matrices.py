m=int(input())
c=[]
d=[]
e=[]
for i in range(2*m):
    a=list(map(int,input().split()))
    c.append(a)
d=c[0:m]
e=c[m:]
for i in range(m):
    for j in range(m):
        if d[i][j]>e[i][j]:
            if j == m-1:
                print(d[i][j]-e[i][j],end="")
            else:
                print(d[i][j]-e[i][j],end=" ")
        else:
            if j == m-1:
                print(e[i][j]-d[i][j],end="")
            else:
                print(e[i][j]-d[i][j],end=" ")
    print()
