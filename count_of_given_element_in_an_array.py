n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n-1,-1,-1):
    if l[i]==k:
        c+=1
print(c)