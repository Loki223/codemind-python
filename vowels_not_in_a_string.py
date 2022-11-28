a=input()
v=['a','e','i','o','u']
s=""
for i in a:
    if i in v and i not in s:
        s+=i
        v.remove(i)
if v==[]:
    print(0)
else:
    print(*v)