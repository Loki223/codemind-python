m,n=map(int,input().split())
even=0
odd=0
for i in range(m):
    k=list(map(int,input().split()))
    for j in range(len(k)):
        if k[j]%2 == 1:
            odd+=k[j]
        else:
            even+=(k[j])
print(even,odd,sep=" ")