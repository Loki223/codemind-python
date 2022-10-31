n=int(input())
v=n**2
a=[]
b=[]
cn=0
while n:
    t=n%10
    a.append(t)
    n=n//10
while v:
    h=v%10
    b.append(h)
    v=v//10
c=[]
m=len(b)
for i in range(0,m-len(a)):#0 1 2
    if b[i]==a[i]:
        cn+=1

if cn==len(a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
