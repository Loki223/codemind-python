n=int(input())
l=list(map(int,input().split()))
even=[i for i in l if i%2==0 ]
odd=[i for i in l if i%2==1]
c=0
for i in range(0,n-2):
    if (l[i] in even and l[i+2] in odd) or (l[i] in odd and l[i+2] in even):
        c+=1
if (l[n-1] in even and l[1] in odd) or (l[n-1] in odd and l[1] in even):
    c+=1
if (l[n-2] in even and l[0] in odd) or (l[n-2] in odd and l[0] in even):
    c+=1
print(c)