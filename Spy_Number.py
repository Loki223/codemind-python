n=int(input())
n=str(n)
s=0
p=1
for i in n:
    s+=int(i)
    p*=int(i)
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")