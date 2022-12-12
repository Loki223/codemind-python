n=int(input())
l=list(map(int,input().split()))
if n%2==1:
    print(*l,end=" ")
    print(0,end=" ")
else:
    print(*l)