n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[i for i in range(a,b+1)]
s=[]
for i in l:
    if i not in l1:
        s.append(i)
if s==[]:
    print(-1)
else:
    print(max(s))