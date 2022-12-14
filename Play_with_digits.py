def s(a):
    f=list(str(a))
    c=0
    for i in f:
        c+=int(i)
    return c
n=int(input())
l=list(map(int,input().split()))
su=0
for i in l:
    su+=s(i)
print(su)