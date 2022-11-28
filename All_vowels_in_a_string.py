a=input()
lv=["a","e","i","o","u"]
uv=["A","E","I","O","U"]
l=u=0
s1=""
s2=""
for i in a:
    if i in lv and i not in s1:
        s1+=i
        l+=1
    if i in uv and i not in s2:
        s2+=i
        u+=1
if l==5 or u == 5:
    print(True)
else:
    print(False)
        