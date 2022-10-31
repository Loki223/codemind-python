n=int(input())
v=n
k=[]
cnt=0
while n:
    i=n%10
    k.append(i)
    n=n//10 
for i in range(len(k)):
    for j in range(len(k)):
        if k[i]!=k[j]:
            cnt+=1
if cnt == len(k)*(len(k)-1):
    print("Unique Number")
else:
    print("Not Unique Number")