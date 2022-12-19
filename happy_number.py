n=int(input())
while True:
    n=str(n)
    l=[int(i)**2 for i in n]
    n=sum(l)
    if n<9:
        break
if n==1 or n==7:
    print(True)
else:
    print(False)