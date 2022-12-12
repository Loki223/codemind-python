n=int(input())
l=list(map(int,input().split()))
c=[l.count(i) for i in l]
l1=[]
for i in range(n):
    if l[i]==c[i] and l[i] not in l1:
        l1.append(l[i])
print(len(l1))
