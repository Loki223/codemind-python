n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[i for i in l if i<=k]
if a==[]:
    print(-1)
else:
    print(sum(a))