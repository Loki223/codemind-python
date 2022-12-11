n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[i for i in range(a,b+1)]
s=0
for i in l:
    if i not in l1:
        s+=1
        print(i,end=" ")
if s==0:
    print(-1)