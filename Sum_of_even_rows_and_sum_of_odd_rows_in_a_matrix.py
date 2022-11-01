m,n=map(int,input().split())
even=0
odd=0
for i in range(m):
    k=list(map(int,input().split()))
    if i%2 == 0:
        odd+=sum(k)
    else:
        even+=sum(k)
print(odd,even,sep=" ")