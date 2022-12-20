n=int(input())
l=list(map(int,input().split()))
e=o=0
for i in l:
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))