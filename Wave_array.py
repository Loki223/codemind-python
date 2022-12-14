n=int(input())
l=list(map(int,input().split()))
c=0
d=0
if n%2==1:
    for j in range(n//2):
        for i in range(1):
            if l[c]<l[c+1] and l[c+1]>l[c+2]:
                d+=1
        c+=2
else:
    for j in range(n//2-1):
        for i in range(1):
            if (l[c]<l[c+1] and l[c+1]>l[c+2]) or (l[c+1]<l[c+2] and l[c]>l[c+1]):
                d+=1
        c+=2
if n%2==1:
    if d!=n//2:
        print("no")
    else:
        print("yes")
else:
    if d!=(n-1)//2:
        print("no")
    else:
        print("yes")