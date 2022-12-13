n=int(input())
l=list(map(int,input().split()))
m,n=map(int,input().split())
if m>n:
    m,n=n,m
a=[i for i in l if i>=m and i<=n]
if a==[]:
    print(-1)
else:
    print(min(a))