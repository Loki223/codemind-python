def vowel(a):
    c=0
    v=["a","e","i","o","u","A","E","I","O","U"]
    for i in a:
        if i in v:
            c+=1
    return c
w=0
a=input().split()
b=[]
for i in a:
    b.append(vowel(i))
for i in b:
    if i==min(b):
        w+=1
print(w)