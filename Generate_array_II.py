n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,n+2,2):
    for j in range(l[i]):
        print(l[c],end=" ")
    c+=2
        