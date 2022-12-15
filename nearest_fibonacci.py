n=int(input())
n1=0
n2=1
s=0
a=[0]
while s<n:
    s=n1+n2
    n1=n2
    n2=s
    a.append(s)
for i in range(len(a)-1):
    if a[i]<n and a[i+1]>n:
        c1=abs(n-a[i])
        c2=abs(na[i+1])
        if c1<c2:
            print(a[i])
        elif c1==c2:
            print(a[i],a[i+1],sep=" ")
        else:
            print(a[i+1])