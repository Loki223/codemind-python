m=int(input())
n=int(input())
for i in range(m,n+1):
    s=str(i)
    c=0
    for j in s:
        if int(j)!=0:
            if i%int(j)==0:
                c+=1
    if c==len(s):
        print(i,end=" ")