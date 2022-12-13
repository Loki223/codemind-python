n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    if i not in e and i%2==0:
        e.append(i)
print(len(e))
