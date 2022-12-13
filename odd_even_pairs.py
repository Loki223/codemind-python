n=int(input())
l=list(map(int,input().split()))
e=[i for i in l if i%2==0]
o=[i for i in l if i%2==1]
m=k=0
while m<len(o) or k<len(e):
    if m<len(o):
        print(o[m],end=" ")
        m+=1
    if k<len(e):
        print(e[k],end=" ")
        k+=1
if n%2==1:
    print(0)