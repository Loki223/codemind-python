n=int(input())
n1=0
n2=1
n3=1
a=[0,1]
while n3<=n:
   a.append(n3)
   n3=n1+n2
   n1=n2
   n2=n3
if n in a:
    print(True)
else:
    print(False)