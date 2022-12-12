n=int(input())
l=list(map(int,input().split()))
k=n-1
if n%2==0:
    for i in range(n//2):
        print(l[i],l[k],end=" ")
        k-=1
else:
    for  i in range((n//2)+1):
        if k==n//2:
            print(l[k],0,end=" ")
        else:
            print(l[i],l[k],end=" ")
        k-=1