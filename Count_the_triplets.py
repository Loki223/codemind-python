t=int(input())
k=[]
for i in range (t):
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    for i in l:
        for j in l:
            if i!=j and i+j in l and ((i,j) not in k and (j,i) not in k):
                k.append((i,j))
                k.append((j,i))
                c+=1
    if c==0:
        print(-1)
    else:
        print(c)
    