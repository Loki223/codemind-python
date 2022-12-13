n=int(input())
l=list(map(int,input().split()))
e=[i for i in l if i%2==0]
o=[i for i in l if i%2==1]
m=k=0
while m<len(e) or k<len(o):
    if m<len(e):
        print(e[m],end=" ")
        m+=1
    if k<len(o):
        print(o[k],end=" ")
        k+=1
if n%2==1:
    print(0)