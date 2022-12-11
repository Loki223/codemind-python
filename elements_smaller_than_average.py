n=int(input())
l=list(map(int,input().split()))
avg=sum(l)//n
l1=[i for i in l if i<=avg]
print(len(l1))