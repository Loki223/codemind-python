n=int(input())
n1=0
n2=1
print(0,1,end=" ")
for i in range(n-2):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")