a=input()
v=["a","e","i","o","u","A","E","I","O","U"]
s=""
for i in a:
    if i in v and i not in s:
        s+=i
        print(i,end=" ")