m,n=map(int,input().split())
c=0
d=[]
for i in range(m):
    a=list(map(int,input().split()))
    d.append(a)
    if sorted(a)==a or sorted(a,reverse=True)==a:
        c+=1
print(c)