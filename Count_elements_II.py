m,n=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1=list(set(l1))
l2=list(set(l2))
a=[i for i in l1 if i not in l2]
b=[i for i in l2 if i not in l1]
print(len(a)+len(b))