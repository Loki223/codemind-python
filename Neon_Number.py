n=int(input())
sq=n**2
sq=str(sq)
s=0
for i in sq:
    s+=int(i)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")