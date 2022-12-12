n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if i%2!=0 and i not in a:
        a.append(i)
        c+=1
print(c)