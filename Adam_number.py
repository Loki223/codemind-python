n=int(input())
r=str(n)
n=str(n**2)
r=int(r[-1:-len(r)-1:-1])
r=r**2
r=str(r)
if n==r[-1:-len(r)-1:-1]:
    print(True)
else:
    print(False)