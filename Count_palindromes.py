n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    s=str(i)
    if s==s[-1:-len(s)-1:-1]:
        c+=1
print(c)