n=int(input())
l=list(map(int,input().split()))
dec=0
k=0
l.reverse()
for i in l:
    dec+=(i*(2**k))
    k+=1
print(dec)