m,n=map(int,input().split())
a=[]
b=[]
for i in range(1,m+1):
    if m%i==0:
        a.append(i)
for i in range(1,n+1):
    if n%i==0:
        b.append(i)
c=[]
for i in a:
    if i in b:
        c.append(i)
print(max(c))