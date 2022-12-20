n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
if a in l:
    print(True)
else:
    print(False)