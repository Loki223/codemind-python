n=int(input())
l=list(map(int,input().split()))
if n%2==0:
    f=l[0:(n//2)]
    s=l[(n//2):len(l)+1]
else:
    f=l[0:(n//2)]
    s=l[(n//2):len(l)]
print(abs(sum(f)-sum(s)))