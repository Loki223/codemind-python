n=int(input())
l=list(map(int,input().split()))
c=[l.count(i) for i in l]
l1=[]
for i in range(n):
    if l[i]==c[i]:
        l1.append(l[i])
k=set(l1)
k=list(k)
if l1==[]:
    print(-1)
else:
    print(min(k),max(k))