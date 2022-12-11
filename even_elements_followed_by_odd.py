n=int(input())
l=list(map(int,input().split()))
even=[i for i in l if i%2==0]
odd=[i for i in l if i%2==1]
print(*even,end=" ")
print(*odd)