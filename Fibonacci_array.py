n=int(input())
l=list(map(int,input().split()))
c=0
if n>3:
    for i in range(n-2):
        if l[i]+l[i+1]==l[i+2]:
            c+=1
        else:
            break
        
    if c==n-2:
        print("yes")
    else:
        print("no")
else:
    print("no")