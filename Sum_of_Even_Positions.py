n=int(input())
l=list(map(int,input().split()))
e=s=0
for i in l:
    if e%2==0:
        s+=i
    e+=1
print(s)