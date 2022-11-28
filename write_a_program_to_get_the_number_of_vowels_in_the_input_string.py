a=input()
v=["a","e","i","o","u","A","E","I","O","U"]
c=0
for i in a:
    if i in v:
        c+=1
if c>0:
    print(c)
else:
    print(0)