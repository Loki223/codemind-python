m,n=map(int,input().split())
su=0
for i in range(m):
    a=list(map(int,input().split()))
    su+=sum(a)
print(su)